import os

from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from .forms import LoginUserForm
from .models import EventModel, RegionalAssociationModel
from .utils import get_order_key_by_token


def index(request):
    return render(request, template_name='web_app/about.html')


def overview(request, order_token: str = 'order_by_date'):
    events_unsorted = EventModel.objects.all()
    order_key = get_order_key_by_token(order_token)
    events = events_unsorted.order_by(order_key, 'start_date') if order_key else events_unsorted
    context = {'events': events,
               }
    return render(request, template_name='web_app/overview.html', context=context)


def associations(request):
    regional_associations = RegionalAssociationModel.objects.all()
    context = {
        'associations': regional_associations,
    }
    return render(request, template_name='web_app/regional_associations.html', context=context)


def concrete_association(request, association_slug):
    association = RegionalAssociationModel.objects.filter(slug=association_slug).first()
    context = {
        'association': association,
        'YANDEX_MAP_API_KEY': os.getenv('YANDEX_MAP_API_KEY'),
    }
    return render(request, template_name='web_app/concrete_association.html', context=context)


class RegisterUser(CreateView):
    pass


class LoginUser(LoginView):
    template_name = 'web_app/login.html'
    form_class = LoginUserForm

    def get_success_url(self):
        return reverse('index')
