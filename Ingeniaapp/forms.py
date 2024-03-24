from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *
from django.forms.widgets import PasswordInput, TextInput
from django.template.loader import render_to_string


class CreateUserForm(UserCreationForm):
    nombre = forms.CharField(max_length=255)
    email = forms.EmailField(required=True)
    apellido = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'nombre', 'apellido']

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Crea el perfil del comprador asociado
            Usuario.objects.create(
                usuario=user,
                correo=user.email,
                nombre=self.cleaned_data['nombre'],
                apellido=self.cleaned_data['apellido'],
            )
        return user



class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())