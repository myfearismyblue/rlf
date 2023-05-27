from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import CharField, TextInput, EmailField, PasswordInput, EmailInput


class LoginUserForm(AuthenticationForm):
    username = CharField(label='Login', widget=TextInput(attrs={'class': 'input-form form-control',
                                                                'placeholder': "Login",
                                                                'id': 'floatingInput',
                                                                'type': "text",
                                                                }))
    password = CharField(label='Password', widget=PasswordInput(attrs={'class': 'input-form form-control',
                                                                       'placeholder': "Password",
                                                                       'id': 'floatingInput',
                                                                       'type': "password",
                                                                       }))


class RegisterUserForm(UserCreationForm):
    username = CharField(label='Login', widget=TextInput(attrs={'class': 'input-form form-control',
                                                                'placeholder': "Login",
                                                                'id': 'floatingInput',
                                                                'type': "text",
                                                                }))
    email = EmailField(label='Email', widget=EmailInput(attrs={'class': 'input-form form-control',
                                                               'placeholder': "Email",
                                                               'id': 'floatingInput',
                                                               'type': "text",
                                                               }))
    password1 = CharField(label='Password', widget=PasswordInput(attrs={'class': 'input-form form-control',
                                                                        'placeholder': "Password",
                                                                        'id': 'floatingInput',
                                                                        'type': "password",
                                                                        }))
    password2 = CharField(label='Password confirmation', widget=PasswordInput(
        attrs={'class': 'input-form form-control',
               'placeholder': "Password confirmation",
               'id': 'floatingInput',
               'type': "password",
               }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
