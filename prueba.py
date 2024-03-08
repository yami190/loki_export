import csv

archivo_csv = 'C:/Users/freddo/Desktop/pre_ahorro.csv'  # Reemplaza con la ruta correcta de tu archivo CSV

with open(archivo_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')  # Especificar el delimitador
    
    next(csv_reader)
    
    for fila in csv_reader:
        if len(fila) >= 6:
            cedula = fila[0]
            codigo = fila[1]
            nombre = fila[2] if len(fila) > 2 else ""
            apor_ahorro = float(fila[3])
            mes = fila[4]
            ano = int(fila[5])
            
            # Haz lo que necesites con las variables separadas
            # Por ejemplo, puedes imprimir sus valores:
            print("Cédula:", cedula)
            print("Código:", codigo)
            print("Nombre:", nombre)
            print("Aporte de ahorro:", apor_ahorro)
            print("Mes:", mes)
            print("Año:", ano)
        else:
            print("La fila no tiene suficientes elementos")