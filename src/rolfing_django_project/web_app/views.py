import os
import uuid
from typing import Dict, Sequence

from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.utils.translation import activate
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView

from .forms import LoginUserForm, RegisterUserForm
from .models import EventModel, RegionalAssociationModel, RolfUser
from .utils import get_order_key_by_token
from rolfing_django_project import settings


def index(request):
    return render(request, template_name='web_app/about.html')


def overview(request, order_token: str = 'order_by_date'):
    events_unsorted = EventModel.objects.filter(end_date__gte=timezone.now())
    order_key = get_order_key_by_token(order_token)
    events = events_unsorted.order_by(order_key, 'start_date') if order_key else events_unsorted
    context = {'events': events,
               }
    return render(request, template_name='web_app/overview.html', context=context)


def archive(request, order_token: str = 'order_by_date'):
    events_unsorted = EventModel.objects.filter(end_date__lt=timezone.now())
    order_key = get_order_key_by_token(order_token)
    events = events_unsorted.order_by(order_key, 'start_date') if order_key else events_unsorted
    context = {'events': events,
               }
    return render(request, template_name='web_app/archive.html', context=context)


def associations(request):
    regional_associations = RegionalAssociationModel.objects.all()
    context = {
        'associations': regional_associations,
    }
    return render(request, template_name='web_app/regional_associations.html', context=context)


def concrete_association(request, association_id):
    association = RegionalAssociationModel.objects.filter(id=association_id).first()
    context = {
        'association': association,
        'YANDEX_MAP_API_KEY': os.getenv('YANDEX_MAP_API_KEY'),
    }
    return render(request, template_name='web_app/concrete_association.html', context=context)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'web_app/register.html'
    success_url = reverse_lazy('login')

    def _generate_register_token(self):
        """Return uuid4 as a hex string len = 32 with prefix set in settings.py """
        self.token = ''.join((settings.ROLF_USER_CONFIRM_PREFIX,  uuid.uuid4().hex, ))
        assert len(self.token) < RolfUser._meta.get_field('confirmation_key').max_length, \
            f'User token has to long length: {len(self.token)}, ' \
            f'but less than {RolfUser.confirmation_key.max_length} is required.'
        return self.token

    def _generate_confirm_link(self, user: RolfUser):
        return self.request.build_absolute_uri(
            reverse_lazy(register_confirmation, kwargs={'token': self.token or None, 'user_id': user.id}))

    def form_valid(self, form):
        """
        Generates a user with unique username and email or gets old user if it's already exist. For new ones sets pwd.
        Generates a token and sets it as well as the generation time.
        Creates and sends confirmation link.
        """

        def _without_keys(dict_: Dict, excluded: Sequence):
            """Excludes keys from given dict. Returns new dict."""
            return {key: dict_[key] for key in dict_ if key not in excluded}

        user, is_new = RolfUser.objects.get_or_create(**_without_keys(form.cleaned_data, ('password1', 'password2',)))
        if not user.is_active or is_new:
            self._generate_register_token()
            if is_new:
                user.set_password(form.cleaned_data['password1'])
            user.confirmation_key = self.token
            user.confirmation_key_time = timezone.now()
            user.save()
            confirmation_link = self._generate_confirm_link(user)
            send_mail(
                subject=_('Please confirm your registration'),
                message=_(f'To proceed registration, please follow this link: {confirmation_link}'),
                recipient_list=[user.email, ],
                from_email='myfearismyblue@gmail.com',
            )
        return HttpResponseRedirect(self.success_url)


def register_confirmation(request, token, user_id):
    user = get_object_or_404(RolfUser, id=user_id)
    too_late = (timezone.now() - user.confirmation_key_time).seconds > settings.ROLF_CONFIRM_DELAY_IN_SEC
    if not too_late and user.confirmation_key == token:
        user.is_active = True
        user.save(update_fields=['is_active', ])
    return HttpResponseRedirect(reverse_lazy('login'))


class LoginUser(LoginView):
    template_name = 'web_app/login.html'
    form_class = LoginUserForm

    def get_success_url(self):
        return reverse('index')


def logout_user(request):
    logout(request)
    return redirect(reverse('login'))


def change_language(request, lang_code):
    activate(lang_code)
    previous_url = request.META.get('HTTP_REFERER') or reverse('index')
    response = redirect(previous_url)
    response.set_cookie('lang_code', value=lang_code)
    return response
