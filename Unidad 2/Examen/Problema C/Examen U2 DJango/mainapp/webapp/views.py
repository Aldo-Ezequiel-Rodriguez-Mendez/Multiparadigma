from django.shortcuts import render
from gestorapp.models import Alumno,Plantel,Docente

# Create your views here.
def inicio(request):
    plantel = Plantel.objects.order_by('id')
    alumno = Alumno.objects.order_by('id')
    docente = Docente.objects.order_by('id')
    return render(request,'index.html',{'plantel':plantel, 'alumno':alumno, 'docente':docente})

def inicioalumno(request):
    alumno = Alumno.objects.order_by('id')
    return render(request,'index_alumno.html',{'alumno':alumno})

def iniciodocente(request):
    docente = Docente.objects.order_by('id')
    return render(request,'index_docente.html',{'docente':docente})

def inicioplantel(request):
    plantel = Plantel.objects.order_by('id')
    return render(request,'index_plantel.html',{'plantel':plantel})