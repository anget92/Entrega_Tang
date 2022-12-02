from django.db import models

class profesor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    profesion=models.CharField(max_length=50)
    anio_experiencia=models.IntegerField()
    fecha_nacimiento=models.DateField()
    email=models.EmailField()

class clase(models.Model):
    nombre=models.CharField(max_length=50)
    intensidad=models.CharField(max_length=50)
    
class cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    genero=models.CharField(max_length=50)
    antiguedad=models.IntegerField()
    fecha_nacimiento=models.DateField()
    email=models.EmailField()
