from django.shortcuts import render


def index(request):
    return render(request, template_name='web_app/about.html')


def overview(request):
    return render(request, template_name='web_app/overview.html')

# Create your views here.
