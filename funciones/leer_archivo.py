# Nombre, Apellido
from funciones.armar_diccionario import armar_diccionario

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
PARA IMPLEMENTAR EN EL MAIN

archivo_entrada1 = open("Cuentos.txt", "r")
archivo_entrada2 = open("La araña negra - tomo 1.txt", "r")
archivo_entrada3 = open("Las 1000 Noches y 1 Noche.txt", "r")
archivo_salida = open("Salida.csv", "w")
archivos = [archivo_entrada1, archivo_entrada2, archivo_entrada3]
i = 0
dic_desordenado = {}
for archivo in archivos:
    diccionario = leer_archivo (archivo, dic_desordenado, i)
    i += 1
guardar(diccionario, archivo_salida)
archivo_entrada1.close()
archivo_entrada2.close()
archivo_entrada3.close()
archivo_salida.close()
"""
