from django.db import models


# Create your models here.

class CuerpoMedico(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=30)
    dia_hora_atencion = models.CharField(max_length=90)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    
class Pacientes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    documento = models.IntegerField()
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

class Consulta(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    consulta_paciente = models.CharField(max_length=150)


