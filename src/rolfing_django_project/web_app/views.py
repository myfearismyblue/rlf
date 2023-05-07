from django.shortcuts import render

from .models import EventModel


def index(request):
    return render(request, template_name='web_app/about.html')


def overview(request):
    events = EventModel.objects.all()
    context = {'events': events,
               }
    return render(request, template_name='web_app/overview.html', context=context)

# Create your views here.
