from django.shortcuts import render, get_object_or_404,redirect
from biblioteca.models import Biblioteca, Autor, Libro, Empleado
from biblioteca.forms import BibliotecaForm, AutorForm, LibroForm, EmpleadoForm

# Create your views here.

#CRUD sucursales
def detalleSucursal(request,id):
    biblioteca = get_object_or_404(Biblioteca,pk=id)
    return render(request,'detalleSucursal.html',{'biblioteca':biblioteca})

def nuevaSucursal(request):
    if request.method == "POST":
        formaBiblioteca = BibliotecaForm(request.POST)
        if formaBiblioteca.is_valid():
            formaBiblioteca.save()
            return redirect('index')
    else:
        formaBiblioteca=BibliotecaForm()
        return render(request,'agregarSucursal.html',{'formaBiblioteca':formaBiblioteca})

def editarSucursal(request,id):
    biblioteca = get_object_or_404(Biblioteca,pk=id)
    if request.method == "POST":
        formaBiblioteca = BibliotecaForm(request.POST,instance=biblioteca)
        if formaBiblioteca.is_valid():
            formaBiblioteca.save()
            return redirect('index')
    else:
        formaBiblioteca = BibliotecaForm(instance=biblioteca)
        return render(request,'editarSucursal.html',{'formaBiblioteca':formaBiblioteca})

def eliminarSucursal(request,id):
    biblioteca = get_object_or_404(Biblioteca,pk=id)
    if biblioteca:
        biblioteca.delete()
    return redirect('index')


#CRUD autores
def detalleAutor(request,id):
    autor = get_object_or_404(Autor,pk=id)
    return render(request,'detalleAutor.html',{'autor':autor})

def nuevoAutor(request):
    if request.method == "POST":
        formaAutor = AutorForm(request.POST)
        if formaAutor.is_valid():
            formaAutor.save()
            return redirect('index')
    else:
        formaAutor=AutorForm()
        return render(request,'agregarAutor.html',{'formaAutor':formaAutor})

def editarAutor(request,id):
    autor = get_object_or_404(Autor,pk=id)
    if request.method == "POST":
        formaAutor = AutorForm(request.POST,instance=autor)
        if formaAutor.is_valid():
            formaAutor.save()
            return redirect('index')
    else:
        formaAutor = AutorForm(instance=autor)
        return render(request,'editarAutor.html',{'formaAutor':formaAutor})

def eliminarAutor(request,id):
    autor = get_object_or_404(Autor,pk=id)
    if autor:
        autor.delete()
    return redirect('index')

#CRUD libros
def detalleLibro(request,id):
    libro = get_object_or_404(Libro,pk=id)
    return render(request,'detalleLibro.html',{'libro':libro})

def nuevoLibro(request):
    if request.method == "POST":
        formaLibro = LibroForm(request.POST)
        if formaLibro.is_valid():
            formaLibro.save()
            return redirect('index')
    else:
        formaLibro=LibroForm()
        return render(request,'agregarLibro.html',{'formaLibro':formaLibro})

def editarLibro(request,id):
    libro = get_object_or_404(Libro,pk=id)
    if request.method == "POST":
        formaLibro = LibroForm(request.POST,instance=libro)
        if formaLibro.is_valid():
            formaLibro.save()
            return redirect('index')
    else:
        formaLibro = LibroForm(instance=libro)
        return render(request,'editarLibro.html',{'formaLibro':formaLibro})

def eliminarLibro(request,id):
    libro = get_object_or_404(Libro,pk=id)
    if libro:
        libro.delete()
    return redirect('index')



#CRUD empleados
def detalleEmpleado(request,id):
    empleado = get_object_or_404(Empleado,pk=id)
    return render(request,'detalleEmpleado.html',{'empleado':empleado})

def nuevoEmpleado(request):
    if request.method == "POST":
        formaEmpleado = EmpleadoForm(request.POST)
        if formaEmpleado.is_valid():
            formaEmpleado.save()
            return redirect('index')
    else:
        formaEmpleado=EmpleadoForm()
        return render(request,'agregarEmpleado.html',{'formaEmpleado':formaEmpleado})

def editarEmpleado(request,id):
    empleado = get_object_or_404(Empleado,pk=id)
    if request.method == "POST":
        formaEmpleado = EmpleadoForm(request.POST,instance=empleado)
        if formaEmpleado.is_valid():
            formaEmpleado.save()
            return redirect('index')
    else:
        formaEmpleado = EmpleadoForm(instance=empleado)
        return render(request,'editarEmpleado.html',{'formaEmpleado':formaEmpleado})

def eliminarEmpleaado(request,id):
    empleado = get_object_or_404(Empleado,pk=id)
    if empleado:
        empleado.delete()
    return redirect('index')