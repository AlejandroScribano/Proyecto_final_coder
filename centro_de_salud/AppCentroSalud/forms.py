from django import forms
from django.forms import fields
from django.forms.forms import Form

#para el registro de usuarios
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MedicoFormulario(forms.Form):
    nombre = forms.CharField(max_length=35)
    apellido = forms.CharField(max_length=30)
    documento = forms.CharField(max_length=15)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=15)
    especialidad = forms.CharField(max_length=15)

class PacientesFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    documento = forms.CharField(max_length=15)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=15)

class ConsultaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=15)
    consulta_paciente = forms.CharField(max_length=150)

#Formulario de registro

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        #saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

#Formulario de edición de usuario

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label='Modificar email')
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        #saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

#Formulario agregar avatar

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)
