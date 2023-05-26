from django.contrib.auth.forms import AuthenticationForm
from django.forms import CharField, TextInput


class LoginUserForm(AuthenticationForm):
    username = CharField(label='Login', widget=TextInput(attrs={'class': 'form-control',
                                                                'placeholder': "Login",
                                                                'id': 'floatingInput',
                                                                'type': "text",
                                                                }))
    password = CharField(label='Password', widget=TextInput(attrs={'class': 'form-control',
                                                                   'placeholder': "Password",
                                                                   'id': 'floatingInput',
                                                                   'type': "password",
                                                                   }))

