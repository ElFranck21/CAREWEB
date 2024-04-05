from django.db import models

# Create your models here.


class Contacto (models.Model):
    nombre=models.CharField(max_length=100)
    correo=models.EmailField()
    descripcion=models.CharField(max_length=1000)

def __str__(self):
    return self.nombre
