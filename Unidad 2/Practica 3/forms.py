from flask import Flask
from flask_wtf import FlaskForm 
from models import Persona,Alumno
from wtforms import StringField,SubmitField  
from wtforms.validators import DataRequired

class PersonaForm(FlaskForm): 
    nombre= StringField('Nombre',validators=[DataRequired()])
    apellido= StringField('Apellido')
    email = StringField('Email',validators=[DataRequired()]) 
    enviar = SubmitField('Enviar')                    
    
    
class AlumnoForm(FlaskForm):
      nombre= StringField('Nombre',validators=[DataRequired()])
      apellido= StringField('Apellido')
      numerodecontrol = StringField('Numerodecontrol',validators=[DataRequired()]) 
      enviar = SubmitField('Enviar')  
    


