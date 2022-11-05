import sys
sys.path.append('./CRUD')

from logger_base import log
class ContratoPersona():
    def __init__(self,id,idpersona,idcontrato) -> None:
        self._id = id
        self._idpersona = idpersona
        self._idcontrato = idcontrato
        pass
    
    def __str__(self) -> str:
        return f"id de la relacion: {self._id}\nid persona: {self._idpersona}\nid contrato: {self._idcontrato}"
    