import time
from time import sleep
from tqdm import tqdm
from conexion import Conexion
from importar import *
from modeloSQL import *

def limpiarTablas():
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
    pass

def funcion3():
    # Simulación de una tercera tarea
    for _ in tqdm(range(8), desc='Función 3'):
        sleep(0.15)

def menu():
    while True:
        print("1. Ejecutar función 1")
        print("2. Ejecutar función 2")
        print("3. Ejecutar función 3")
        print("0. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            limpiarTablas()
        elif opcion == '2':
            funcion2()
        elif opcion == '3':
            funcion3()
        elif opcion == '0':
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu()