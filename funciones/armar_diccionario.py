def armar_diccionario (lista, dic_desordenado, nro):
    for palabra in lista:
        palabra = palabra.casefold()
        if palabra in dic_desordenado:
            dic_desordenado[palabra][nro] += 1
        else:
            dic_desordenado[palabra] = [0, 0, 0]
            dic_desordenado[palabra][nro] += 1
    return dic_desordenado