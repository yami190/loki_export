import psycopg2

class Conexion:
    @staticmethod
    def ConexionBaseDeDatos():
        try:
            conexion = psycopg2.connect(user='postgres',
                                       password='hkmff6y',
                                       host='localhost',
                                       database='valhalla_old',
                                       port='5432',
                                       client_encoding='UTF8')  # Especifica la codificación aquí
            cursor = conexion.cursor()
            cursor.execute("SELECT pg_encoding_to_char(encoding) FROM pg_database WHERE datname = 'valhalla';;")
            miResultado = cursor.fetchall()
            #print(miResultado)
            return conexion
        except psycopg2.Error as error:
            print(error)

# Llama al método para establecer la conexión al momento de importar el módulo
Conexion.ConexionBaseDeDatos()