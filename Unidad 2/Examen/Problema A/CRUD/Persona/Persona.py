import sys
sys.path.append('./CRUD')

from logger_base import log
class Persona():
    def __init__(self,id,nombre,edad,correo) -> None:
        self._id = id
        self._nombre = nombre
        self._edad = edad
        self._correo = correo
        pass
    
    def __str__(self) -> str:
        return f"id: {self._id}\nnombre: {self._nombre}\nedad: {self._edad}correo: {self._correo}"
    