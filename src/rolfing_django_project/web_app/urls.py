from django.urls import path, re_path

from .views import index, overview, associations, concrete_association, LoginUser

urlpatterns = [
    re_path(r'login[/]?', LoginUser.as_view(), name='login'),
    re_path(r'overview[/]?$', overview, name='overview'),
    path(r'overview/<order_token>', overview, name='overview'),
    re_path(r'about[/]?', index, name='about'),
    path(r'associations/<slug:association_slug>', concrete_association, name='concrete_association'),
    re_path(r'associations[/]?$', associations, name='associations'),
    re_path(r'', index, name='index'),
]

