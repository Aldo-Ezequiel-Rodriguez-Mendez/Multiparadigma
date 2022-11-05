import sys
sys.path.append('./CRUD')

from logger_base import log

class Contrato():
    def __init__(self,id,nocontrato,costo,fechaini,fechafin) -> None:
        self._id = id
        self._nocontrato = nocontrato
        self._costo = costo
        self._fechaini = fechaini
        self._fechafin = fechafin
        pass
    
    def __str__(self) -> str:
        return f"id: {self._id}\nnocontrato: {self._nocontrato}\ncosto: {self._costo}\nfechaini: {self._fechaini} \ncosto: {self._fechafin} "
    