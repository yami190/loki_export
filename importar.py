import csv
import psycopg2

# Ruta del archivo CSV
#archivo_csv = 'ruta/del/archivo.csv'
archivo_csv = 'C:/Users/freddo/Desktop/pre_ahorro.csv'

# Datos de conexión a la base de datos PostgreSQL
conexion = psycopg2.connect(
    host="localhost",
    port="5432",
    database="valhalla",
    user="postgres",
    password="123456"
)

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()



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

        #print(fila)
        
        # Insertar la fila en la tabla
        cursor.execute(
            'INSERT INTO pre_ahorro (cedula, codigo, nombre, apor_ahorro, mes, ano) VALUES (%s, %s, %s, %s, %s, %s)',
            (cedula, codigo, nombre, apor_ahorro, mes, ano)
        )

# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()