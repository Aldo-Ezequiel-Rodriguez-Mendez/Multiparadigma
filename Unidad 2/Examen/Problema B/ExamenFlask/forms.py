from flask import Flask
from flask_wtf import FlaskForm 
from models import Profesor,Empleado 
from wtforms import StringField,SubmitField  
from wtforms.validators import DataRequired

 
class ProfesorForm(FlaskForm): 
    nombre= StringField('Nombre',validators=[DataRequired()])
    materia= StringField('Materia')
    escuela= StringField('Escuela',validators=[DataRequired()]) 
    enviar = SubmitField('Enviar')                    
       
class EmpleadoForm(FlaskForm):
      nombre= StringField('Nombre',validators=[DataRequired()])
      cargo= StringField('Cargo')
      departamento = StringField('Departamento',validators=[DataRequired()]) 
      enviar = SubmitField('Enviar') 
    


