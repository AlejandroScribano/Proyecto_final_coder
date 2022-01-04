from django.db import models


# Create your models here.

class Persona(models.Model):
 nombre = models.CharField(max_length=30)
 apellido = models.CharField(max_length=30)
 documento = models.IntegerField(blank=True, null=True)
 email = models.EmailField()
 telefono = models.CharField(max_length=15)
 
class Medico(models.Model):
 nombre = models.CharField(max_length=35)
 apellido = models.CharField(max_length=30)
 documento = models.IntegerField(blank=True, null=True)
 email = models.EmailField()
 telefono = models.CharField(max_length=15)
 especialidad = models.CharField(max_length=15)

class Consulta(models.Model):
  nombre = models.CharField(max_length=30)
  apellido = models.CharField(max_length=30)
  email = models.EmailField()
  telefono = models.CharField(max_length=15)
  consulta_paciente = models.CharField(max_length=130)

