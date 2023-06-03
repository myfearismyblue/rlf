from django.urls import path, re_path

from .views import index, overview, associations, concrete_association, LoginUser, logout_user, RegisterUser, archive, \
    change_language, register_confirmation

urlpatterns = [
    re_path(r'login[/]?$', LoginUser.as_view(), name='login'),
    re_path(r'logout[/]?$', logout_user, name='logout'),
    re_path(r'register[/]?$', RegisterUser.as_view(), name='register'),
    path(r'register_confirmation/<token>/<user_id>', register_confirmation, name='register_confirmation'),
    re_path(r'overview[/]?$', overview, name='overview'),
    path(r'overview/<order_token>', overview, name='overview'),
    re_path(r'archive[/]?$', archive, name='archive'),
    path(r'archive/<order_token>', archive, name='archive'),
    re_path(r'about[/]?$', index, name='about'),
    path(r'associations/id<int:association_id>', concrete_association, name='concrete_association'),
    re_path(r'associations[/]?$', associations, name='associations'),
    path(r'language/<lang_code>', change_language),
    re_path(r'', index, name='index'),
]
