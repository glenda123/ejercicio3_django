from django.db import models

# Create your models here.
from areas.models import Area
from managers.models import Manager
# from datetime import date

class Empleado(models.Model):
    nombre=models.CharField(max_length=200)
    direccion=models.CharField(max_length=300)
    correo=models.CharField(max_length=100)
    telefono=models.CharField(max_length=20, default='')
    edad=models.IntegerField(null=True)

    area=models.ForeignKey(Area, on_delete=models.CASCADE, default='')
    managers=models.ManyToManyField(Manager, related_name='empleados')
    created=models.DateTimeField(auto_created=True, null=True)
    updated=models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nombre
