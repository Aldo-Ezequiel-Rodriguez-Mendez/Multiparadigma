from django.contrib import admin
from biblioteca.models import Biblioteca,Libro,Autor,Empleado

from biblioteca.models import Biblioteca

# Register your models here.
admin.site.register(Biblioteca)
admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(Empleado)
