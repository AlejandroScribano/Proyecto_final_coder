from django.db import models

#para el avatar
from django.contrib.auth.models import User


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

#Para el Avatar

class Avatar(models.Model):
  #vinculo con el usuario
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  #subcarpeta avatares de media
  imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
