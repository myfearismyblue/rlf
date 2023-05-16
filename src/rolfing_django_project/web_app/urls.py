from django.urls import path, re_path

from .views import index, overview, associations, concrete_association

urlpatterns = [
    re_path(r'overview[/]?', overview, name='overview'),
    re_path(r'about[/]?', index, name='about'),
    path(r'associations/<slug:association_slug>', concrete_association, name='concrete_association'),
    re_path(r'associations[/]?$', associations, name='associations'),
    re_path(r'', index, name='index'),
]

