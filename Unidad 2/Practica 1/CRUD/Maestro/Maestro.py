import sys
sys.path.append('./CRUD')

from logger_base import log
class Maestro():
    def __init__(self,id,nombre,materia) -> None:
        self._id = id
        self._nombre = nombre
        self._materia = materia
        pass
    
    def __str__(self) -> str:
        return f"id: {self._id}\nnombre: {self._nombre}\nmateria impartida: {self._materia}"
    