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

def contarPreMovimiento():
    connec = Conexion.ConexionBaseDeDatos()
    cursor = connec.cursor()
    consulta = 'SELECT COUNT(*) FROM mov_temp'
    cursor.execute(consulta)
    resultado = cursor.fetchone()[0]
    return resultado

def eliminaRegistroAnterior():
    connec = Conexion.ConexionBaseDeDatos()
    cursor = connec.cursor()
    delete= 'DELETE FROM mov_temp;'
    cursor.execute(delete)
    connec.commit()
    connec.close()

def insertarAportes():

    connec = Conexion.ConexionBaseDeDatos()
    cursor = connec.cursor()
    insertar = "INSERT INTO mov_temp (cedula, codigo, nombres, apor_ahorro, mes, ano) " \
               "SELECT cedula, codigo, nombre, SUM(apor_ahorro), mes, ano " \
               "FROM pre_ahorro " \
               "GROUP BY cedula, codigo, nombre, mes, ano;"
    cursor.execute(insertar)
    connec.commit()
    connec.close()

def insertarPrestamos():

    connec = Conexion.ConexionBaseDeDatos()
    cursor = connec.cursor()
    insertar ="UPDATE mov_temp SET apor_presta = (SELECT SUM(apor_presta) FROM pre_prestamos WHERE pre_prestamos.cedula = mov_temp.cedula);"
    cursor.execute(insertar)
    connec.commit()
    connec.close()

def insertarSeguro():

    connec = Conexion.ConexionBaseDeDatos()
    cursor = connec.cursor()
    insertar ="UPDATE mov_temp SET seguro = ( SELECT SUM(seguro) FROM pre_seguro WHERE pre_seguro.cedula = mov_temp.cedula );"
    cursor.execute(insertar)
    connec.commit()
    connec.close()




