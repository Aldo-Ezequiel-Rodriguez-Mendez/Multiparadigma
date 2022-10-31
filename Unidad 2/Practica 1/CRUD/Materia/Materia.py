import sys
sys.path.append('./CRUD')

from logger_base import log
class Materia():
    def __init__(self,id,nombre,creditos) -> None:
        self._id = id
        self._nombre = nombre
        self._creditos = creditos
        pass
    
    def __str__(self) -> str:
        return f"id: {self._id}\nnombre: {self._nombre}\ncreditos: {self._creditos}"
    