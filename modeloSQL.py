from conexion import *

def concultaDeRegistro():
    connec = Conexion.ConexionBaseDeDatos()
    cursor = connec.cursor()
    consulta = 'SELECT COUNT(*) FROM pre_ahorro'
    cursor.execute(consulta)
    resultado = cursor.fetchone()[0]
    return resultado
    #print("Se agregaron {}, nuevos".format(total_filas))


