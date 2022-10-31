import sys
sys.path.append('./CRUD')

from logger_base import log
from conexion import Conexion

class CursorPool:
    def __init__(self) -> None:
        self._conexion = None
        self._cursor = None
        
    def __enter__(self):
        log.debug("Inicio metodo with")
        self._conexion = Conexion.ObtConexionPool()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    def __exit__(self,tipo_excepcion,valor_excepcion,detalles_excepcion):
        log.debug("Se ejecuta exit")
        if valor_excepcion:
            self._conexion.rollback()
        else:
            self._conexion.commit()
        self._cursor.close()
        Conexion.LiberarConexion(self._conexion)
        
if __name__ == "__main__":
    with CursorPool as cursor:
        log.debug("Dentro del bloqie with")
        cursor.execute("SELECT * FROM estudiante")
        log.debug(cursor.fetchall())