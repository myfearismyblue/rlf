from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import CharField, TextInput, EmailField, PasswordInput, EmailInput
from django.utils.translation import pgettext_lazy, gettext_lazy as _


class LoginUserForm(AuthenticationForm):
    username = CharField(label=pgettext_lazy('form_content', 'Login') , widget=TextInput(attrs={'class': 'input-form form-control',
                                                                                                'placeholder': pgettext_lazy('form_content',"Login"),
                                                                                                'id': 'floatingInput',
                                                                                                'type': "text",
                                                                                                }))
    password = CharField(label=_('Password'), widget=PasswordInput(attrs={'class': 'input-form form-control',
                                                                          'placeholder': _("Password"),
                                                                          'id': 'floatingInput',
                                                                          'type': "password",
                                                                          }))


class RegisterUserForm(UserCreationForm):
    username = CharField(label=pgettext_lazy('form_content','Login'), widget=TextInput(attrs={'class': 'input-form form-control',
                                                                                              'placeholder': pgettext_lazy('form_content',"Login"),
                                                                                              'id': 'floatingInput',
                                                                                              'type': "text",
                                                                                              }))
    email = EmailField(label=_('Email'), widget=EmailInput(attrs={'class': 'input-form form-control',
                                                                  'placeholder': _("Email"),
                                                                  'id': 'floatingInput',
                                                                  'type': "text",
                                                                  }))
    password1 = CharField(label=_('Password'), widget=PasswordInput(attrs={'class': 'input-form form-control',
                                                                           'placeholder': _("Password"),
                                                                           'id': 'floatingInput',
                                                                           'type': "password",
                                                                           }))
    password2 = CharField(label=_('Password confirmation'), widget=PasswordInput(
        attrs={'class': 'input-form form-control',
               'placeholder': _("Password confirmation"),
               'id': 'floatingInput',
               'type': "password",
               }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
