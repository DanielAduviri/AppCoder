from django.db import models

class Curso(models.Model):

    nombre= models.CharField("nombre",max_length=50)
    camada= models.IntegerField()

class Alumno(models.Model):

    nombre= models.CharField("nombre", max_length=100)
    apellido= models.CharField("apellido", max_length=50)
    fecha_inscripcion= models.DateField("fecha", auto_now=False, auto_now_add=False)

class Profesor(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    profesion= models.CharField(max_length=50)

class Entregable(models.Model):
    nombre= models.CharField(max_length=40)
    fechaDeEntrega=  models.DateField()
    entregad=models.BooleanField()