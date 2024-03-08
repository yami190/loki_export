import csv
from conexion import Conexion

def pre_ahorro():
    # Ruta del archivo CSV
    archivo_csv = 'C:/Users/freddo/Desktop/pre_ahorro.csv'

    # Establecer la conexión a la base de datos PostgreSQL
    connec = Conexion.ConexionBaseDeDatos()
    cursor = connec.cursor()


    # Abrir el archivo CSV
    with open(archivo_csv, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')  # Especificar el delimitador
        
        next(csv_reader)
        
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
