import sys
sys.path.append('./CRUD')

from Estudiante import Estudiante
from conexion import Conexion
from logger_base import log
from cursorDePool import CursorPool  

class EstudianteDao():
    _SELECT = "SELECT * FROM estudiante ORDER BY id"
    _INSERT = "INSERT INTO estudiante(nombre,semestre) VALUES(%s,%s)"
    _UPDATE = "UPDATE estudiante SET  nombre = %s,semestre = %s WHERE id = %s"
    _DELETE = "DELETE FROM estudiante WHERE id = %s"
    
    @classmethod
    def SELECT(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            estudiantes = []
            for r in registros:
                estudiante = Estudiante(r[0],r[1],r[2])
                estudiantes.append(estudiante)
            return estudiantes

    @classmethod
    def INSERT(cls,estudiante):
        with CursorPool() as cursor:
            valores = (estudiante._nombre,estudiante._semestre)
            cursor.execute(cls._INSERT,valores)
            return cursor.rowcount
        
    @classmethod
    def UPDATE(cls,estudiante):
        with CursorPool() as cursor:
            valores = (estudiante._nombre,estudiante._semestre,estudiante._id)
            cursor.execute(cls._UPDATE,valores)
            return cursor.rowcount
        
    @classmethod
    def DELETE(cls,estudiante):
        with CursorPool() as cursor:
            valores = (estudiante._id,)
            cursor.execute(cls._DELETE,valores)
            return cursor.rowcount
        
if __name__ == '__main__':
    #INSERT
    estudiante1 = Estudiante(id="",nombre="EJEMPLO",semestre="9")
    estudiantesInsertados = EstudianteDao.INSERT(estudiante1)
    log.debug(f"Estudiantes Insertados {estudiantesInsertados}")
    #UPDATE
    estudiante1 = Estudiante(id="1",nombre="AAAAA",semestre="A")
    estudiantesActualizados = EstudianteDao.UPDATE(estudiante1)
    log.debug(f"Estudiantes Actualizadas {estudiantesActualizados}")
    #DELETE
    estudiantesEliminados = EstudianteDao.DELETE(estudiante1)
    log.debug(f"Estudaintes Eliminados {estudiantesEliminados}")
    #SELECT
    estudiantes = EstudianteDao.SELECT()
    for e in estudiantes:
        log.debug(e)
