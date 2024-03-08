import time
from time import sleep
from tqdm import tqdm
from conexion import Conexion
from importar import *
from modeloSQL import *

def limpiarTablas():
    connec = Conexion.ConexionBaseDeDatos()
    cursor = connec.cursor()

    #pre_ahorro()
    # Simulación de una tarea
    # Obtener la cantidad to1tal de filas en la tabla
    # consulta = 'SELECT COUNT(*) FROM pre_ahorro'
    # cursor.execute(consulta)
    # total_filas = cursor.fetchone()[0]
    total_filas = concultaDeRegistro()
    eliminar = 'DELETE FROM pre_ahorro;'
    if total_filas > 0:
        respuesta = input("Se encontraron {} filas. ¿Desea seguir ingresando registros? (s/n): ".format(total_filas))
        if respuesta.lower() == 's':
                try:
                    cursor.execute(eliminar)
                    connec.commit()  # Confirmar los cambios
                    pre_ahorro()
                    resultado = concultaDeRegistro()
                    print("Se eliminaron todas las filas de la tabla pre_ahorro y se ingresaron {}, nuevos registros".format(resultado))

                except ValueError as e:
                    print("Error al eliminar las filas de la tabla 'pre_ahorro':", e)
            
        else:
            # Salir del programa
           pass
    else:
        # No se eliminaron filas
        pre_ahorro()
        resultado = concultaDeRegistro()
        print (resultado)

    # if respuesta.lower() == 's':
    
    
    connec.close()
    #return respuesta.lower() == 's'
    

    


    
       

def funcion2():
    # Simulación de otra tarea
    for _ in tqdm(range(5), desc='Función 2'):
        sleep(0.2)

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