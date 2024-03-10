import os
from conexion import *

def generar_archivo(opcion, mes, ano):
        #while True:
            if opcion == '1':
                
                try:
                    connec = Conexion.ConexionBaseDeDatos()
                    with connec.cursor() as cursor:
                        cursor.execute("""SELECT LPAD(a.cedula::text, 8, '0') as cedula, RPAD(a.nombres, 40, ' ') as nombres,
                                1 as codigo, LPAD(REPLACE(CAST(b.apor_ahorro AS text), '.', ''), 10, ' ') as apor_patrono,
                                LPAD(REPLACE(CAST(b.apor_ahorro AS text), '.', ''), 10, ' ') as apor_ahorro,
                                LPAD(COALESCE(REPLACE(CAST(b.apor_presta AS text), '.', ''), '0'), 10, ' ') as apor_presta,
                                LPAD(COALESCE(REPLACE(CAST(b.seguro AS text), '.', ''), '0'), 10, ' ') as seguro
                            FROM
                                socios a
                            INNER JOIN
                                movimientos b ON a.cedula = b.cedula
                            WHERE b.mes = %s AND b.ano = %s AND a.codigo BETWEEN 1 AND 29;""",
                    (mes, ano))
                        consulta = cursor.fetchall()
                    ruta_archivo = os.path.join('C:/Users/sistemas/Desktop/data/txt/', f'GOB_{mes}_{ano}.TXT')
                    # Abrir un archivo en modo de escritura
                    with open(ruta_archivo, mode="w") as txt:
                    #ruta_archivo = os.path.join('/ruta/completa/', f'GOB_{mes}_{ano}.TXT')
                        for a in consulta:
                            txt.write(''.join(str(x) for x in a))
                            txt.write("\n")
                    print(f"Archivo se ha generado en {ruta_archivo}")

                finally:
                    # Cerrar la conexión a la base de datos
                    connec.close()
            elif opcion == '2':

                try:
                    connec = Conexion.ConexionBaseDeDatos()
                    with connec.cursor() as cursor:
                        cursor.execute("""SELECT LPAD(a.cedula::text, 8, '0') as cedula, RPAD(a.nombres, 40, ' ') as nombres,
                                1 as codigo, LPAD(REPLACE(CAST(b.apor_ahorro AS text), '.', ''), 10, ' ') as apor_patrono,
                                LPAD(REPLACE(CAST(b.apor_ahorro AS text), '.', ''), 10, ' ') as apor_ahorro,
                                LPAD(COALESCE(REPLACE(CAST(b.apor_presta AS text), '.', ''), '0'), 10, ' ') as apor_presta,
                                LPAD(COALESCE(REPLACE(CAST(b.seguro AS text), '.', ''), '0'), 10, ' ') as seguro
                            FROM
                                socios a
                            INNER JOIN
                                movimientos b ON a.cedula = b.cedula
                            WHERE b.mes = %s AND b.ano = %s AND a.codigo BETWEEN 30 AND 33;""",
                    (mes, ano))
                        consulta = cursor.fetchall()
                    
                    # # Abrir un archivo en modo de escritura
                    # with open(f'ISP_{mes}_{ano}.TXT', mode="w") as txt:
                    #     for a in consulta:
                    #         txt.write(''.join(str(x) for x in a))
                    #         txt.write("\n")
                    ruta_archivo = os.path.join('C:/Users/sistemas/Desktop/data/txt/', f'ISP_{mes}_{ano}.TXT')
                    # Abrir un archivo en modo de escritura
                    with open(ruta_archivo, mode="w") as txt:
                    #ruta_archivo = os.path.join('/ruta/completa/', f'GOB_{mes}_{ano}.TXT')
                        for a in consulta:
                            txt.write(''.join(str(x) for x in a))
                            txt.write("\n")
                    print(f"Archivo se ha generado en {ruta_archivo}")

                finally:
                    # Cerrar la conexión a la base de datos
                    connec.close()
            else:
                #break
                 print("Opción inválida. Intente nuevamente, no seas mamon")
            # else:
            #     print("Opción inválida. Intente nuevamente, no seas mamon")