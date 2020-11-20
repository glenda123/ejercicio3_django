from django.db import models
# from datetime import date
# Create your models here.
class Area(models.Model):
    nombre=models.CharField(max_length=150)
    direccion=models.CharField(max_length=300)
    telefono=models.CharField(max_length=20)
    created=models.DateTimeField(auto_created=True, null=True)
    updated=models.DateTimeField( auto_now=True, null=True)

    def __str__(self):
        return self.nombre