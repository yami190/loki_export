from time import sleep
from tqdm import tqdm
from conexion import Conexion
from importar import *
from modeloSQL import *

def importarNomina():
    connec = Conexion.ConexionBaseDeDatos()
    cursor = connec.cursor()

    eliminarAhorro = 'DELETE FROM pre_ahorro;'
    eliminarPrestamos= 'DELETE FROM pre_prestamos;'
    eliminarSeguro= 'DELETE FROM pre_seguro;'
    totalAhorro = contarPreAhorro()
    totalPresta = contarPrePrestamos()
    totalSeguro = contarPreSeguro()
    if totalAhorro > 0 or totalPresta > 0 or totalSeguro > 0:
        respuesta = input("Se encontraron {} filas en pre_ahorro, {} filas en pre_prestamos, {} filas en pre_seguro. ¿Desea seguir ingresando registros? (s/n): ".format(totalAhorro,totalPresta,totalSeguro))
        if respuesta.lower() == 's':
                try:
                    cursor.execute(eliminarAhorro)
                    cursor.execute(eliminarPrestamos)
                    cursor.execute(eliminarSeguro)
                    connec.commit()  # Confirmar los cambios
                    pre_ahorro()
                    pre_prestamos()
                    pre_seguro()
                    contAhorro = contarPreAhorro()
                    contPrestamos = contarPrePrestamos()
                    conSeguro = contarPreSeguro()
                    print("Total pre_ahorro {0} nuevos registros,Total pre_prestamos {1}, nuevos registros,Total pre_seguro {2}, nuevos registros,".format(contAhorro,contPrestamos,conSeguro))

                except ValueError as e:
                    print("Error al eliminar las filas de la tabla 'pre_ahorro':", e)
            
        else:
            # Salir del programa
           pass
    else:
        # Si no consigue Registros lo ingresa sin pregntar
        try:
            pre_ahorro()
            pre_prestamos()
            pre_seguro()
            ahorro = contarPreAhorro()
            prestamos = contarPrePrestamos()
            seguro = contarPreSeguro()
            print("Total pre_ahorro {0} nuevos registros,Total pre_prestamos {1}, nuevos registros,Total pre_seguro {2}, nuevos registros,".format(ahorro,prestamos,seguro))
        except ValueError as e:
            print("Error :", e)
    
    
    connec.close()
    

def ArmarPremovimiento():
    premovimieto = contarPreMovimiento()
    if premovimieto > 0:
        respuesta = input("Se encontraron {} . ¿Desea seguir ingresando registros? (s/n): ".format(premovimieto))
        if respuesta.lower() == 's':
                try:
                    eliminaRegistroAnterior()
                    insertarAportes()
                    insertarPrestamos()
                    insertarSeguro()
                    premovimieto = contarPreMovimiento()
                    print("Total nuevos registros ingresados {}".format(premovimieto))

                except ValueError as e:
                    print("Error al eliminar las filas de la tabla 'pre_ahorro':", e)
            
        else:
            # Salir del programa
           pass
    else:
        # Si no consigue Registros lo ingresa sin pregntar
        try:
            insertarAportes()
            insertarPrestamos()
            insertarSeguro()
            premovimieto = contarPreMovimiento()
            print("Total nuevos registros ingresados {}".format(premovimieto))
        except ValueError as e:
            print("Error :", e)
    


def ajusteGobernacion():
    connec = Conexion.ConexionBaseDeDatos()
    cursor = connec.cursor()
    ajuste = 'update mov_temp set apor_ahorro = apor_ahorro / 2'
    cursor.execute(ajuste)
    connec.commit() 
    

def menu():
    while True:
        print("1. Importar Nomina")
        print("2. Procesar Premovimiento")
        print("3. Montar en Producción")
        print("0. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            importarNomina()
        elif opcion == '2':
            ArmarPremovimiento()
        elif opcion == '3':
            ajusteGobernacion()
        elif opcion == '0':
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu()