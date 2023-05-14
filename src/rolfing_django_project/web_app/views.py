from django.shortcuts import render

from .models import EventModel, RegionalAssociationModel


def index(request):
    return render(request, template_name='web_app/about.html')


def overview(request):
    events = EventModel.objects.all()
    context = {'events': events,
               }
    return render(request, template_name='web_app/overview.html', context=context)


def associations(request):
    regional_associations = RegionalAssociationModel.objects.all()
    context = {
        'associations': regional_associations,
    }
    return render(request, template_name='web_app/regional_associations.html', context=context)

# Create your views here.
