from django.forms import ModelForm,EmailInput
from biblioteca.models import Biblioteca, Autor, Libro, Empleado

class BibliotecaForm(ModelForm):
    class Meta:
        model = Biblioteca
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }

class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }

class LibroForm(ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }

class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }