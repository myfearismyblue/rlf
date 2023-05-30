import os

from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.utils.translation import activate
from django.views.generic import CreateView

from .forms import LoginUserForm, RegisterUserForm
from .models import EventModel, RegionalAssociationModel
from .utils import get_order_key_by_token


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
