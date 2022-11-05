from django.db import models

# Create your models here.
class Carrera(models.Model):
    nombre = models.CharField(max_length=255)
    semestres = models.IntegerField()
    def __str__(self) -> str:
        return f'Carrera {self.id}: {self.nombre} {self.semestres}'

class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    numero = models.IntegerField()
    def __str__(self) -> str:
        return f'Domicilio {self.id}: {self.calle} {self.numero}'

class Alumno(models.Model):
    nombre = models.CharField(max_length=255)
    semestre = models.IntegerField()
    carrera = models.ForeignKey(Carrera,on_delete=models.SET_NULL,null=True)
    domicilio = models.ForeignKey(Domicilio,on_delete=models.SET_NULL,null=True)
    def __str__(self) -> str:
        return f'Alumno {self.id}: {self.nombre} {self.semestre}'

class Docente(models.Model):
    nombre = models.CharField(max_length=255)
    materia = models.CharField(max_length=255)
    carrera = models.ForeignKey(Carrera,on_delete=models.SET_NULL,null=True)
    domicilio = models.ForeignKey(Domicilio,on_delete=models.SET_NULL,null=True)
    def __str__(self) -> str:
        return f'Docente {self.id}: {self.nombre} {self.materia}'

class Plantel(models.Model):
    nombre_institucion = models.CharField(max_length=255)
    campus = models.IntegerField()
    def __str__(self) -> str:
        return f'Plantel {self.id}: {self.nombre_institucion} {self.campus}'