from django.db import models
# from datetime import date
# Create your models here.
class Manager(models.Model):
    nombre=models.CharField(max_length=200)
    direccion=models.CharField(max_length=300)
    telefono=models.CharField(max_length=20)
    correo=models.CharField(max_length=100)
    edad=models.IntegerField(null=True)
    created=models.DateTimeField(auto_created=True, null=True)
    updated=models.DateTimeField( auto_now=True, null=True)

    def __str__(self):
        return self.nombre