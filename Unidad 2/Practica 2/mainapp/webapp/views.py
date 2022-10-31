from django.shortcuts import render
from biblioteca.models import Biblioteca,Autor,Libro,Empleado

# Create your views here.
def inicio(request):
    biblioteca = Biblioteca.objects.order_by('id')
    autor = Autor.objects.order_by('id')
    libro = Libro.objects.order_by('id')
    empleado = Empleado.objects.order_by('id')
    return render(request,'index.html',{'biblioteca':biblioteca, 'autor':autor, 'libro':libro, 'empleado':empleado})