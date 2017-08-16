from django.db import models

# Create your models here.

class Usuario(models.Model):
    carne = models.IntegerField(null=False)
    nombre = models.CharField(max_length=64)
    correo =  models.EmailField(max_length=64)
    contrasena = models.CharField(max_length=64)
    horasPendientes = models.IntegerField()
    horasRealizadas = models.IntegerField()
    admin = models.BooleanField()

class Actividad(models.Model):
    nombre = models.CharField(max_length=64, null=False)
    descripcion = models.CharField(max_length=255, null=False, default="Datos de la Actividad:")
    date = models.DateTimeField()
    horas = models.IntegerField()
    carne = models.IntegerField()

class AsigActividad(models.Model):
    idActividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
