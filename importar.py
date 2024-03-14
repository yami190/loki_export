import csv
from conexion import Conexion

def pre_ahorro():
    # Ruta del archivo CSV
    #archivo_csv = 'C:/Users/freddo/Desktop/pre_ahorro.csv'
    archivo_csv = 'C:/Users/sistemas/Desktop/data/AHORRO.csv'

    # Establecer la conexión a la base de datos PostgreSQL
    connec = Conexion.ConexionBaseDeDatos()
    cursor = connec.cursor()


    # Abrir el archivo CSV
    with open(archivo_csv, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')  # Especificar el delimitador
        
        #next(csv_reader)
        
        for fila in csv_reader:
            cedula = fila[0]
            codigo = fila[1]
            nombre = fila[2] if len(fila) > 2 else ""
            apor_ahorro = float(fila[3])
            mes = fila[4]
            ano = int(fila[5])


            # Insertar la fila en la tabla
            cursor.execute(
                'INSERT INTO pre_ahorro (cedula, codigo, nombre, apor_ahorro, mes, ano) VALUES (%s, %s, %s, %s, %s, %s)',
                (cedula, codigo, nombre, apor_ahorro, mes, ano)
            )

    # Confirmar los cambios y cerrar la conexión
    connec.commit()
    connec.close()

def pre_prestamos():
    # Ruta del archivo CSV
    #archivo_csv = 'C:/Users/freddo/Desktop/pre_ahorro.csv'
    archivo_csv = 'C:/Users/sistemas/Desktop/data/PRESTAMOS.csv'
    print(archivo_csv)

    # Establecer la conexión a la base de datos PostgreSQL
    connec = Conexion.ConexionBaseDeDatos()
    cursor = connec.cursor()


    # Abrir el archivo CSV
    with open(archivo_csv, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')  # Especificar el delimitador
        
        #next(csv_reader)
        
        for fila in csv_reader:
            cedula = fila[0]
            codigo = fila[1]
            nombre = fila[2] if len(fila) > 2 else ""
            apor_presta = float(fila[3])
            mes = fila[4]
            ano = int(fila[5])

            # Insertar la fila en la tabla
            cursor.execute(
                'INSERT INTO pre_prestamos (cedula, codigo, nombre, apor_presta, mes, ano) VALUES (%s, %s, %s, %s, %s, %s)',
                (cedula, codigo, nombre, apor_presta, mes, ano)
            )
            


    # Confirmar los cambios y cerrar la conexión
    connec.commit()
    connec.close()

def pre_seguro():
    # Ruta del archivo CSV
    #archivo_csv = 'C:/Users/freddo/Desktop/pre_ahorro.csv'
    archivo_csv = 'C:/Users/sistemas/Desktop/data/SEGURO.csv'

    # Establecer la conexión a la base de datos PostgreSQL
    connec = Conexion.ConexionBaseDeDatos()
    cursor = connec.cursor()


    # Abrir el archivo CSV
    with open(archivo_csv, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')  # Especificar el delimitador
        
        #next(csv_reader)
        
        for fila in csv_reader:
            cedula = fila[0]
            codigo = fila[1]
            nombre = fila[2] if len(fila) > 2 else ""
            seguro = float(fila[3])
            mes = fila[4]
            ano = int(fila[5])

            cursor.execute(
                'INSERT INTO pre_seguro (cedula, codigo, nombre, seguro, mes, ano) VALUES (%s, %s, %s, %s, %s, %s)',
                (cedula, codigo, nombre, seguro, mes, ano)
            )
            

    # Confirmar los cambios y cerrar la conexión
    connec.commit()
    connec.close()
