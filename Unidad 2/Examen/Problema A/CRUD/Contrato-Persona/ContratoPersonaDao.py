import sys
sys.path.append('./CRUD')

from ContratoPersona import ContratoPersona
from conexion import Conexion
from logger_base import log
from cursorDePool import CursorPool  

class ContratoPersonaDao():
    _SELECT = "SELECT * FROM contratopersona ORDER BY id"
    _INSERT = "INSERT INTO contratopersona(idcontrato, idpersona) VALUES(%s,%s)"
    _SELECT

    @classmethod
    def SELECT(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            contratopersonas = []
            for r in registros:
                contratopersona = ContratoPersona(r[0],r[1],r[2])
                contratopersonas.append(contratopersona)
            return contratopersonas

    @classmethod
    def INSERT(cls,contratopersona):
        with CursorPool() as cursor:
            valores = (contratopersona._idcontrato,contratopersona._idpersona)
            cursor.execute(cls._INSERT,valores)
            return cursor.rowcount
            
if __name__ == '__main__':
    #INSERT
    contratopersona1 = ContratoPersona(id="",idcontrato="2",idpersona="7")
    relacionInsertada = ContratoPersonaDao.INSERT(contratopersona1)
    log.debug(f"Relacion Insertada {relacionInsertada}")
    #SELECT
    relaciones = ContratoPersonaDao.SELECT()
    for r in relaciones:
        log.debug(r)