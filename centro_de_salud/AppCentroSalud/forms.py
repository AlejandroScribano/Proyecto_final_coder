from django import forms
from django.forms.forms import Form

class CuerpoMedicoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    especialidad = forms.CharField(max_length=30)
    dia_hora_atencion = forms.CharField(max_length=90)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=15)

class PacientesFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    documento = forms.IntegerField()
    email = forms.EmailField()
    telefono = forms.CharField(max_length=15)

class ConsultaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=15)
    consulta_paciente = forms.CharField(max_length=150)