# Nombre, Apellido
from funciones.armar_diccionario import armar_diccionario
from funciones.guardar import guardar

"""
Función: leer_archivo
Parámetros:
    archivo:
    dic_desordenado:
    nro:
    LONGITUD_PALABRA:
Salidas:
"""


def leer_archivo(archivo, dic_desordenado, nro, LONGITUD_PALABRA):
    lista = []
    linea = archivo.readline()
    a = True
    while a:
        linea = linea.rstrip("\n").rstrip(",").rsplit(" ")
        for palabra in linea:
            if palabra.isalpha() and palabra.isascii() and len(palabra) == LONGITUD_PALABRA:
                lista.append(palabra)
        linea = archivo.readline()
        if not linea:
            a = False
    diccionario = armar_diccionario(lista, dic_desordenado, nro)
    return diccionario


"""
Función: unificar_archivos
Parámetros:
    LONGITUD_PALABRA:
Salidas:
    diccionario:
"""

def unificar_archivos(LONGITUD_PALABRA):
    with open("archivos/Cuentos.txt", "r", encoding="utf-8") as archivo_entrada1, open("archivos/La araña negra - tomo 1.txt", "r", encoding="utf-8") as archivo_entrada2, open("archivos/Las 1000 Noches y 1 Noche.txt", "r", encoding="utf-8") as archivo_entrada3, open("archivos/palabras.csv", "w") as archivo_salida:
        archivos = [archivo_entrada1, archivo_entrada2, archivo_entrada3]
        i = 0
        dic_desordenado = {}
        for archivo in archivos:
            diccionario = leer_archivo(archivo, dic_desordenado, i, LONGITUD_PALABRA)
            i += 1
        guardar(diccionario, archivo_salida)
    return diccionario
