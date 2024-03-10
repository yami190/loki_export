from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from conexion import *

def Nuevos_exportar_a_pdf():
    try:
        connec = Conexion.ConexionBaseDeDatos()
        with connec.cursor() as cursor:
            cursor.execute("""SELECT a.cedula, a.nombres, b.nombre as nomina
                            FROM mov_temp a
                            INNER JOIN nominas b ON a.codigo = b.codigo
                            WHERE a.cedula NOT IN (SELECT cedula FROM socios)""")
            consulta = cursor.fetchall()

        # Crear un nuevo archivo PDF
        ruta_pdf = "C:/Users/sistemas/Desktop/data/pdf/pdNuevos.pdf"
        doc = SimpleDocTemplate(ruta_pdf, pagesize=letter)

        # Definir un estilo personalizado para el texto
        estilo = ParagraphStyle(
            name="EstiloPersonalizado",
            fontSize=12,
            fontName="Helvetica-Bold",
            textColor=colors.black
        )

        # Crear una lista para almacenar los elementos del PDF
        elementos = []

        # Agregar los datos a la lista de elementos
        for row in consulta:
            cedula, nombres, nomina = row
            texto = f"<b>Cédula:</b> {cedula}<br/><b>Nombres:</b> {nombres}<br/><b>Nómina:</b> {nomina}<br/><br/>"
            parrafo = Paragraph(texto, estilo)
            elementos.append(parrafo)

        # Agregar los elementos al documento PDF
        doc.build(elementos)

        print("Archivo PDF generado: resultado.pdf",ruta_pdf )

    finally:
        # Cerrar la conexión a la base de datos
        connec.close()

def Retirados_exportar_a_pdf():
    try:
        connec = Conexion.ConexionBaseDeDatos()
        with connec.cursor() as cursor:
            cursor.execute("""SELECT a.cedula, a.nombres, b.nombre AS nomina
                                FROM socios a
                                inner join movimientos c on a.cedula = c.cedula
                                INNER JOIN nominas b ON a.codigo = b.codigo
                                WHERE a.cedula NOT IN (SELECT cedula FROM mov_temp)
                                AND c.mes = 1
                                AND c.ano = 2024;""")
            consulta = cursor.fetchall()

        # Crear un nuevo archivo PDF
        ruta_pdf = "C:/Users/sistemas/Desktop/data/pdf/pdretirados.pdf"
        doc = SimpleDocTemplate(ruta_pdf, pagesize=letter)

        # Definir un estilo personalizado para el texto
        estilo = ParagraphStyle(
            name="EstiloPersonalizado",
            fontSize=12,
            fontName="Helvetica-Bold",
            textColor=colors.black
        )

        # Crear una lista para almacenar los elementos del PDF
        elementos = []

        # Agregar los datos a la lista de elementos
        for row in consulta:
            cedula, nombres, nomina = row
            texto = f"<b>Cédula:</b> {cedula}<br/><b>Nombres:</b> {nombres}<br/><b>Nómina:</b> {nomina}<br/><br/>"
            parrafo = Paragraph(texto, estilo)
            elementos.append(parrafo)

        # Agregar los elementos al documento PDF
        doc.build(elementos)

        print("Archivo PDF generado: resultado.pdf",ruta_pdf )

    finally:
        # Cerrar la conexión a la base de datos
        connec.close()