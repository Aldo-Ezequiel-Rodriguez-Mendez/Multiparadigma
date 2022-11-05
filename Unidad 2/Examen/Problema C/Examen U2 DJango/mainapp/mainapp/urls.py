"""mainapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import inicio, inicioalumno, iniciodocente,inicioplantel
from gestorapp.views import detalleAlumno,editarAlumno,nuevoAlumno,detalleDocente,editarDocente,nuevoDocente,detallePlantel,editarPlantel,nuevoPlantel, eliminarAlumno,eliminarDocente,eliminarPlantel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio,name='index'),
    path('',inicioalumno,name='index_alumno'),
    path('',iniciodocente,name='index_docente'),
    path('',inicioplantel,name='index_plantel'),
    path('detalle_alumno/<int:id>', detalleAlumno),
    path('nuevo_alumno', nuevoAlumno),
    path('editar_alumno/<int:id>', editarAlumno),
    path('eliminar_alumno/<int:id>',eliminarAlumno),
    path('detalle_docente/<int:id>', detalleDocente),
    path('nuevo_docente', nuevoDocente),
    path('editar_docente/<int:id>', editarDocente),
    path('eliminar_docente/<int:id>',eliminarDocente),
    path('detalle_plantel/<int:id>', detallePlantel),
    path('nuevo_plantel', nuevoPlantel),
    path('editar_plantel/<int:id>', editarPlantel),
    path('eliminar_plantel/<int:id>',eliminarPlantel)
]
