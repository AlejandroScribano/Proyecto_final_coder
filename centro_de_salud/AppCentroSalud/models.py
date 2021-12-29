from django.db import models


# Create your models here.

class Persona (models.Model):
 nombre = models.CharField(max_length=30)
 apellido = models.CharField(max_length=30)
 documento = models.IntegerField(blank=True, null=True)
 email = models.EmailField()
 telefono = models.CharField(max_length=15)
 
class Medico(models.Model):
 idPersona = models.IntegerField(blank=True, null=True)
 idEspecialidad = models.CharField(max_length=10)


class Especialidad(models.Model):
 nombreEspecialidad = models.CharField(max_length=10)

class Pacientes(models.Model):
 idPersona = models.IntegerField(blank=True, null=True)

class Consulta(models.Model):
 idPaciente = models.IntegerField(blank=True, null=True)
 idMedico = models.IntegerField(blank=True, null=True)
 consulta_paciente = models.CharField(max_length=150)

