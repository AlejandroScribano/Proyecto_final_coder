from django.db import models


# Create your models here.

class Persona(models.Model):
 nombre = models.CharField(max_length=30)
 apellido = models.CharField(max_length=30)
 documento = models.IntegerField(blank=True, null=True)
 email = models.EmailField()
 telefono = models.CharField(max_length=15)
 def __str__(self):
  return f"NOMBRE: {self.nombre} APELLIDO: {self.apellido} DOCUMENTO: {self.documento} EMAIL: {self.email} TELEFONO: {self.telefono}"
 
class Medico(models.Model):
 nombre = models.CharField(max_length=35)
 apellido = models.CharField(max_length=30)
 documento = models.IntegerField(blank=True, null=True)
 email = models.EmailField()
 telefono = models.CharField(max_length=15)
 especialidad = models.CharField(max_length=15)
 def __str__(self):
  return f"NOMBRE: {self.nombre} APELLIDO: {self.apellido} DOCUMENTO: {self.documento} EMAIL: {self.email} TELEFONO: {self.telefono} ESPECIALIDAD: {self.especialidad}"

class Consulta(models.Model):
  nombre = models.CharField(max_length=30)
  apellido = models.CharField(max_length=30)
  email = models.EmailField()
  telefono = models.CharField(max_length=15)
  consulta_paciente = models.CharField(max_length=130)
  def __str__(self):
    return f"NOMBRE: {self.nombre} APELLIDO: {self.apellido} EMAIL: {self.email} TELEFONO: {self.telefono} CONSULTA: {self.consulta_paciente}"

