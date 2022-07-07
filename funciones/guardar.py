# Ditrani, Elías Nicolás
"""
Función: guardar
Parámetros:
    diccionario: diccionario con las palabras candidatas
    archivo: archivo donde se guardarán las palabras y las veces que aparece en cada archivo
"""


def guardar (diccionario, archivo):
    dic_ordenado = sorted (diccionario)
    for palabra in dic_ordenado:
        palabra, uno, dos, tres = palabra, str(diccionario[palabra][0]), str(diccionario[palabra][1]), str(diccionario[palabra][2])
        archivo.write(palabra+","+uno+","+dos+","+tres+"\n")
