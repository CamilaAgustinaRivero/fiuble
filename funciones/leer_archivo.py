# Ditrani, Elías Nicolás
from funciones.armar_diccionario import armar_diccionario
from funciones.guardar import guardar

"""
Función: leer_archivo
Parámetros: 
    archivo: un archivo de texto para leer
    dic_desordenado: un diccionario en el que se guardarán las palabras candidatas
    nro: numero de archivo que se esta leyendo
    LONGITUD_PALABRA: longitud de la palabra candidata
Salidas:
    diccionario: un diccionario con las palabras candidatas
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
    LONGITUD_PALABRA: logitud de la palabra candidata
Salidas:
    diccionario: diccionario con las palabras candidatas
"""


def unificar_archivos(LONGITUD_PALABRA):
    with open("../utiles/Cuentos.txt", "r", encoding="utf-8") as archivo_entrada1, open(
            "../utiles/La araña negra - tomo 1.txt", "r", encoding="utf-8") as archivo_entrada2, open(
            "../utiles/Las 1000 Noches y 1 Noche.txt", "r", encoding="utf-8") as archivo_entrada3, open(
        "../archivos_generados/palabras.csv", "w", encoding="utf-8") as archivo_salida:
        archivos = [archivo_entrada1, archivo_entrada2, archivo_entrada3]
        i = 0
        dic_desordenado = {}
        for archivo in archivos:
            diccionario = leer_archivo(archivo, dic_desordenado, i, LONGITUD_PALABRA)
            i += 1
        guardar(diccionario, archivo_salida)
    return diccionario
