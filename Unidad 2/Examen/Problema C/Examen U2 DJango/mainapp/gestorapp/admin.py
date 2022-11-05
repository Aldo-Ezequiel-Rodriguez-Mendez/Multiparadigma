from django.contrib import admin
from gestorapp.models import Domicilio,Plantel,Alumno,Docente,Carrera
# Register your models here.
admin.site.register(Plantel)
admin.site.register(Carrera)
admin.site.register(Domicilio)
admin.site.register(Alumno)
admin.site.register(Docente)