from django.db import models

# Create your models here.

class Biblioteca(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    def __str__(self) -> str:
        return f'Sucursal {self.id}: {self.nombre} {self.direccion} {self.telefono} {self.email}'

class Autor(models.Model):
    nombre = models.CharField(max_length=255)
    cantidad_libros = models.IntegerField()
    def __str__(self) -> str:
        return f'Autor {self.id}: {self.nombre} {self.cantidad_libros}'

class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    editorial = models.CharField(max_length=255)
    disponibilidad = models.IntegerField()
    autor = models.ForeignKey(Autor,on_delete=models.SET_NULL,null=True)
    def __str__(self) -> str:
        return f'Libro {self.id}: {self.titulo} {self.editorial} {self.disponibilidad}'

class Empleado(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    sueldo = models.FloatField()
    def __str__(self) -> str:
        return f'Empleado {self.id}: {self.nombre} {self.apellido} {self.sueldo}'