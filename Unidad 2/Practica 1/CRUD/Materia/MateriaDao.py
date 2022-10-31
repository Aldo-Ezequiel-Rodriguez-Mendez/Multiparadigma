import sys
sys.path.append('./CRUD')

from Materia import Materia
from conexion import Conexion
from logger_base import log
from cursorDePool import CursorPool  

class MateriaDao():
    _SELECT = "SELECT * FROM materia ORDER BY id"
    _INSERT = "INSERT INTO materia(nombre, creditos) VALUES(%s,%s)"
    _UPDATE = "UPDATE materia SET  nombre = %s, creditos = %s WHERE id = %s"
    _DELETE = "DELETE FROM materia WHERE id = %s"
    
    @classmethod
    def SELECT(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            materias = []
            for r in registros:
                materia = Materia(r[0],r[1],r[2])
                materias.append(materia)
            return materias

    @classmethod
    def INSERT(cls,materia):
        with CursorPool() as cursor:
            valores = (materia._nombre,materia._creditos)
            cursor.execute(cls._INSERT,valores)
            return cursor.rowcount
        
    @classmethod
    def UPDATE(cls,materia):
        with CursorPool() as cursor:
            valores = (materia._nombre,materia._creditos,materia._id)
            cursor.execute(cls._UPDATE,valores)
            return cursor.rowcount
        
    @classmethod
    def DELETE(cls,materia):
        with CursorPool() as cursor:
            valores = (materia._id,)
            cursor.execute(cls._DELETE,valores)
            return cursor.rowcount
        
if __name__ == '__main__':
    # #INSERT
    # materia1 = Materia(id="",nombre="Lenguajes y Automatas I",creditos="5")
    # materiasInsertadas = MateriaDao.INSERT(materia1)
    # log.debug(f"Materias Insertadas {materiasInsertadas}")
    # #UPDATE
    # materia1 = Materia(id="4",nombre="Calculo integral",creditos="4")
    # materiasActualizadas = MateriaDao.UPDATE(materia1)
    # log.debug(f"Materias Actualizadas {materiasActualizadas}")
    # #DELETE
    # materiasEliminadas = MateriaDao.DELETE(materia1)
    # log.debug(f"Materias Eliminadas {materiasEliminadas}")
    #SELECT
    materias = MateriaDao.SELECT()
    for m in materias:
        log.debug(m)