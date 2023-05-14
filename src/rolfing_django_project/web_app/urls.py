from django.contrib import admin
from django.urls import path, include, re_path

from .views import index, overview, associations

urlpatterns = [
    re_path(r'overview[/]?', overview, name='overview'),
    re_path(r'about', index, name='about'),
    re_path(r'associations', associations, name='associations'),
    re_path(r'^\w*[/]?', index, name='index'),
]

