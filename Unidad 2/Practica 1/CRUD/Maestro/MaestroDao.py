import sys
sys.path.append('./CRUD')

from Maestro import Maestro
from conexion import Conexion
from logger_base import log
from cursorDePool import CursorPool  

class MaestroDao():
    _SELECT = "SELECT * FROM maestro ORDER BY id"
    _INSERT = "INSERT INTO maestro(nombre, materia) VALUES(%s,%s)"
    _UPDATE = "UPDATE maestro SET  nombre = %s, materia = %s WHERE id = %s"
    _DELETE = "DELETE FROM maestro WHERE id = %s"
    
    @classmethod
    def SELECT(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            maestros = []
            for r in registros:
                maestro = Maestro(r[0],r[1],r[2])
                maestros.append(maestro)
            return maestros

    @classmethod
    def INSERT(cls,maestro):
        with CursorPool() as cursor:
            valores = (maestro._nombre,maestro._materia)
            cursor.execute(cls._INSERT,valores)
            return cursor.rowcount
        
    @classmethod
    def UPDATE(cls,maestro):
        with CursorPool() as cursor:
            valores = (maestro._nombre,maestro._materia,maestro._id)
            cursor.execute(cls._UPDATE,valores)
            return cursor.rowcount
        
    @classmethod
    def DELETE(cls,maestro):
        with CursorPool() as cursor:
            valores = (maestro._id,)
            cursor.execute(cls._DELETE,valores)
            return cursor.rowcount
        
if __name__ == '__main__':
    # #INSERT
    # maestro1 = Maestro(id="",nombre="Bruno Lopez Takeyas",materia="Estructura de Datos")
    # maestrosInsertados = MaestroDao.INSERT(maestro1)
    # log.debug(f"Maestros Insertados {maestrosInsertados}")
    #UPDATE
    maestro1 = Maestro(id="12",nombre="Luis",materia="Programacion multiparadigma")
    # maestrosActualizados = MaestroDao.UPDATE(maestro1)
    # log.debug(f"Maestros Actualizados {maestrosActualizados}")
    #DELETE
    maestrosEliminados = MaestroDao.DELETE(maestro1)
    log.debug(f"Maestros Eliminados {maestrosEliminados}")
    #SELECT
    maestros = MaestroDao.SELECT()
    for m in maestros:
        log.debug(m)