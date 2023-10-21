from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    link = forms.CharField(max_length=100)
    description = forms.CharField(max_length=300)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'description', 'link']


class Profile(UserChangeForm):
    username = forms.CharField(label='Usuario')
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repetir la contraseña', widget=forms.PasswordInput)
    link = forms.CharField(max_length=100)
    description = forms.CharField(max_length=300)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'description', 'link']
        
class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje' : forms.Textarea(attrs={'class': 'form-control'}),
        }