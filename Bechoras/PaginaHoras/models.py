from django.db import models

#

class Usuario(models.Model):
    carnet = models.IntegerField()
    nombre = models.CharField(max_length=64)
    correo =  models.EmailField(max_length=64)
    contrasena = models.CharField(max_length=64)
    horasPendientes = models.IntegerField()
    horasRealizadas = models.IntegerField()
    admin = models.BooleanField()


    def __str__(self):

        return self. nombre  + '-' + self.  correo

class Actividad(models.Model):
    idActividad = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=64)
    date = models.DateTimeField()
    horas = models.IntegerField()
    carne = models.IntegerField()



class AsigActividad(models.Model):
    idAsigActividad = models.IntegerField(primary_key=True)
    idActividad = models.IntegerField()
    idActividad = models.IntegerField()