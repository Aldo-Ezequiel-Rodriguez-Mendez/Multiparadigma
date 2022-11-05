import sys
sys.path.append('./CRUD')

from Persona import Persona
from conexion import Conexion
from logger_base import log
from cursorDePool import CursorPool  

class PersonaDao():
    _SELECT = "SELECT * FROM persona ORDER BY id"
    _INSERT = "INSERT INTO persona(nombre, edad, correo) VALUES(%s,%s,%s)"
    _UPDATE = "UPDATE persona SET  nombre = %s, edad = %s, correo = %s WHERE id = %s"
    _DELETE = "DELETE FROM persona WHERE id = %s"
    
    @classmethod
    def SELECT(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            personas = []
            for r in registros:
                persona = Persona(r[0],r[1],r[2],r[3])
                personas.append(persona)
            return personas

    @classmethod
    def INSERT(cls,persona):
        with CursorPool() as cursor:
            valores = (persona._nombre,persona._edad,persona._correo)
            cursor.execute(cls._INSERT,valores)
            return cursor.rowcount
        
    @classmethod
    def UPDATE(cls,persona):
        with CursorPool() as cursor:
            valores = (persona._nombre,persona._edad,persona._correo,persona._id)
            cursor.execute(cls._UPDATE,valores)
            return cursor.rowcount
        
    @classmethod
    def DELETE(cls,persona):
        with CursorPool() as cursor:
            valores = (persona._id,)
            cursor.execute(cls._DELETE,valores)
            return cursor.rowcount
        
if __name__ == '__main__':
    #INSERT
    persona1 = Persona(id="",nombre="Aldo",edad="21",correo="Aldo@outlook.com")
    personasInsertadas = PersonaDao.INSERT(persona1)
    log.debug(f"Personas Insertadas {personasInsertadas}")
    #UPDATE
    persona1 = Persona(id="2",nombre="PersonaActualizada",edad="21",correo="personaActualizada@outlook.com")
    personasActualizadas = PersonaDao.UPDATE(persona1)
    log.debug(f"Personas Actualizadas {personasActualizadas}")
    #DELETE
    personasEliminadas = PersonaDao.DELETE(persona1)
    log.debug(f"Personas Eliminadas {personasEliminadas}")
    #SELECT
    personas = PersonaDao.SELECT()
    for p in personas:
        log.debug(p)