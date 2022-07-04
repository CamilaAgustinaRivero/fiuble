# Nombre, Apellido
"""
Función: guardar
Parámetros:
    diccionario:
    archivo:
Salidas:
"""


def guardar (diccionario, archivo):
    dic_ordenado = sorted (diccionario)
    for palabra in dic_ordenado:
        palabra, uno, dos, tres = palabra, str(diccionario[palabra][0]), str(diccionario[palabra][1]), str(diccionario[palabra][2])
        archivo.write(palabra+","+uno+","+dos+","+tres+"\n")
