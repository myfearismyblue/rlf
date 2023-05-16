import os

from django.shortcuts import render

from .models import EventModel, RegionalAssociationModel


def index(request):
    return render(request, template_name='web_app/about.html')


def overview(request):
    events = EventModel.objects.all().order_by('start_date')
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

# Create your views here.
