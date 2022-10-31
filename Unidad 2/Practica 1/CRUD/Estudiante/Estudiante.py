import sys
sys.path.append('./CRUD')

from logger_base import log
class Estudiante():
    def __init__(self,id,nombre,semestre) -> None:
        self._id = id
        self._nombre = nombre
        self._semestre = semestre
        pass
    
    def __str__(self) -> str:
        return f"id: {self._id}\nnombre: {self._nombre}\nsemestre: {self._semestre}"
    