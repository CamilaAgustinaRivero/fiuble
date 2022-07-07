# Ditrani, Elías Nicolás
"""
Función: armar_diccionario
Parámetros:
    lista: lista con las palabras candidatas
    dic_desordenado: diccionario donde se salvarán las palabras
    nro: número de archivo que se esta leyendo
Salidas:
    dic_desordenado: regresa el diccionario actualizado con las nuevas palabras
"""


def armar_diccionario(lista, dic_desordenado, nro):
    for palabra in lista:
        palabra = palabra.casefold()
        if palabra in dic_desordenado:
            dic_desordenado[palabra][nro] += 1
        else:
            dic_desordenado[palabra] = [0, 0, 0]
            dic_desordenado[palabra][nro] += 1
    return dic_desordenado
