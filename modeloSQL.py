from conexion import *

def contarPreAhorro():
    connec = Conexion.ConexionBaseDeDatos()
    cursor = connec.cursor()
    consulta = 'SELECT COUNT(*) FROM pre_ahorro'
    cursor.execute(consulta)
    resultado = cursor.fetchone()[0]
    return resultado

def contarPrePrestamos():
    connec = Conexion.ConexionBaseDeDatos()
    cursor = connec.cursor()
    consulta = 'SELECT COUNT(*) FROM pre_prestamos'
    cursor.execute(consulta)
    resultado = cursor.fetchone()[0]
    return resultado

def contarPreSeguro():
    connec = Conexion.ConexionBaseDeDatos()
    cursor = connec.cursor()
    consulta = 'SELECT COUNT(*) FROM pre_seguro'
    cursor.execute(consulta)
    resultado = cursor.fetchone()[0]
    return resultado




