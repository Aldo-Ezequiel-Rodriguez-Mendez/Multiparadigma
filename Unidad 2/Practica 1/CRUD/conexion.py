import psycopg2 as pg
import sys
from logger_base import log
from psycopg2 import pool

class Conexion:
    
    _DATABASE = 'Practica1'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DBPORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _POOL = None
    
    _CONEXION = None
    _CURSOR = None
    
    @classmethod
    def ObtPool(cls):
        if cls._POOL is None:
            try:
                cls._POOL = pool.SimpleConnectionPool(cls._MIN_CON,
                    cls._MAX_CON,
                    host = cls._HOST,
                    user = cls._USERNAME,
                    password = cls._PASSWORD,
                    port = cls._DBPORT,
                    database = cls._DATABASE
                )
                log.debug(f"Creacion del pool {cls._POOL}")
                return cls._POOL
            except Exception as e:
                log.error(f"Ocurrio un error en la creacion de pool {e}")
        else:
            return cls._POOL
    
    @classmethod
    def ObtConexionPool(cls):
        Conexion = cls.ObtPool().getconn()
        log.debug(f"Conexion Obtenida: {Conexion}")
        return Conexion
    
    @classmethod
    def LiberarConexion(cls,conexion):
        cls.ObtPool().putconn(conexion)
        log.debug(f"Conexion regresada: {conexion}")
    
    @classmethod
    def CloseCon(cls,conexion):
        cls.ObtPool().putconn(conexion)
        log.debug(f"Conexion regresada")
    
    @classmethod
    def cerrarConexiones(cls):
        cls.ObtPool().closeall()


if __name__ == '__main__':
    con1 = Conexion.ObtConexionPool()
    con2 = Conexion.ObtConexionPool()