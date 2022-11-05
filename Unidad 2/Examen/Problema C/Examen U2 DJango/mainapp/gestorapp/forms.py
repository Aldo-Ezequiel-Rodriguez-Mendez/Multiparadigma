from pydoc import plain
from django.forms import ModelForm,EmailInput
from gestorapp.models import Plantel,Carrera,Domicilio,Alumno,Docente

class PlantelForm(ModelForm):
    class Meta:
        model = Plantel
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }

class CarreraForm(ModelForm):
    class Meta:
        model = Carrera
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }

class DomicilioForm(ModelForm):
    class Meta:
        model = Domicilio
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }

class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }

class DocenteForm(ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }