from serializer import Serializer
from app import db 
class Persona (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    email = db.Column(db.String(250))
    
    def __str__(self) -> str:
        return (f'ID:{self.id},'
                f'Nombre:{self.nombre},'
                f'Apellido:{self.apellido},'
                f'Email:{self.email}')
        
  
class Alumno (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    numerodecontrol = db.Column(db.String(250))
    
    def __str__(self) -> str:
        return (f'ID:{self.id},'
                f'Nombre:{self.nombre},'
                f'Apellido:{self.apellido},'
                f'Numerodecontrol:{self.numerodecontrol}')


class Michi (db.Model,Serializer):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    raza = db.Column(db.String(250))
    color = db.Column(db.String(250))

    def __str__(self) -> str:
        return (f'ID:{self.id},'
                f'Nombre:{self.nombre},'
                f'Raza:{self.raza},'
                f'Color:{self.color}')
        
        #pip install flask-wtf
        #pip install Flask-Migrate
        