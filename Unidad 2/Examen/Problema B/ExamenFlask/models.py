from serializer import Serializer
from app import db 

#crear CRUD de dos entidades usando formularios 
# profesor (formulario)
class Profesor (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    materia = db.Column(db.String(250))
    escuela = db.Column(db.String(250))
    
    def __str__(self) -> str:
        return (f'ID:{self.id},'
                f'Nombre:{self.nombre},'
                f'Materia:{self.materia},'
                f'Escuela:{self.escuela}'    
                )
#Empleado (formulario)         
class Empleado (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    cargo = db.Column(db.String(250))
    departamento = db.Column(db.String(250))
    
    
    def __str__(self) -> str:
        return (f'ID:{self.id},'
                f'Nombre:{self.nombre},'
                f'Cargo:{self.cargo},'
                f'Departamento:{self.departamento}'
                )


class Pasajero (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    companiavuelo = db.Column(db.String(250))

    def __str__(self) -> str:
        return (f'ID:{self.id},'
                f'Nombre:{self.nombre},'
                f'Companiavuelo:{self.companiavuelo}')
        
        
        
class Director (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    escuela = db.Column(db.String(250))

    def __str__(self) -> str:
        return (f'ID:{self.id},'
                f'Nombre:{self.nombre},'
                f'Escuela:{self.escuela}')
        
        
        #http 
class Cliente (db.Model,Serializer):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    empresa = db.Column(db.String(250))
    
    def __str__(self) -> str:
        return (f'ID:{self.id},'
                f'Nombre:{self.nombre},'
                f'Empresa:{self.empresa}')   
                     
        #pip install flask-wtf
        #pip install Flask-Migrate
        