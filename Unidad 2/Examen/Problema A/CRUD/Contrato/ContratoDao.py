import sys
sys.path.append('./CRUD')

from Contrato import Contrato
from conexion import Conexion
from logger_base import log
from cursorDePool import CursorPool  

class ContratoDao():
    _SELECT = "SELECT * FROM contrato ORDER BY id"
    _INSERT = "INSERT INTO contrato(nocontrato,costo,fechaini,fechafin) VALUES(%s,%s,%s,%s)"
    _UPDATE = "UPDATE contrato SET  nocontrato = %s,costo = %s, fechaini = %s, fechafin = %s WHERE id = %s"
    _DELETE = "DELETE FROM contrato WHERE id = %s"
    
    @classmethod
    def SELECT(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            contratos = []
            for r in registros:
                contrato = Contrato(r[0],r[1],r[2],r[3],r[4])
                contratos.append(contrato)
            return contratos

    @classmethod
    def INSERT(cls,contrato):
        with CursorPool() as cursor:
            valores = (contrato._nocontrato,contrato._costo,contrato._fechaini,contrato._fechafin)
            cursor.execute(cls._INSERT,valores)
            return cursor.rowcount
        
    @classmethod
    def UPDATE(cls,contrato):
        with CursorPool() as cursor:
            valores = (contrato._nocontrato,contrato._costo,contrato._fechaini,contrato._fechafin,contrato._id)
            cursor.execute(cls._UPDATE,valores)
            return cursor.rowcount
        
    @classmethod
    def DELETE(cls,contrato):
        with CursorPool() as cursor:
            valores = (contrato._id,)
            cursor.execute(cls._DELETE,valores)
            return cursor.rowcount
        
if __name__ == '__main__':
    #INSERT
    contrato1 = Contrato(id="5",nocontrato="3",costo="1000",fechaini="02/02/2022",fechafin="09/04/2023")
    contratosInsertados = ContratoDao.INSERT(contrato1)
    log.debug(f"Contratos Insertados {contratosInsertados}")
    #UPDATE
    contrato1 = Contrato(id="1",nocontrato="9",costo="200",fechaini="10/01/2022",fechafin="01/08/2022")
    contratosActualizados = ContratoDao.UPDATE(contrato1)
    log.debug(f"Contratos Actualizadas {contratosActualizados}")
    #DELETE
    contratosEliminados = ContratoDao.DELETE(contrato1)
    log.debug(f"Contratos Eliminados {contratosEliminados}")
    #SELECT
    contratos = ContratoDao.SELECT()
    for c in contratos:
        log.debug(c)
