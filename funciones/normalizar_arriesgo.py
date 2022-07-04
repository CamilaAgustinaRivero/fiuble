#Federico Salvador
"""
Función: normalizar_palabra
Parámetros:
    arriesgo: cadena de caracteres que contiene un arriesgo ingresado por el usuario.
Salidas:
    Devuelve la palabra ingresada sin tildes para su procesamiento en el programa.
"""

def normalizar_palabra(arriesgo):
    resultado = ''
    vocales_tildadas = ['Á','É','Í','Ó','Ú']

    for caracter in arriesgo:
        if caracter in vocales_tildadas:
            if caracter == 'Á':
                resultado+='A'
            elif caracter == 'É':
                resultado+='E'
            elif caracter == 'Í':
                resultado+='I'
            elif caracter == 'Ó':
                resultado+='O'
            else: resultado+='U'
        else: resultado += caracter

    arriesgo = resultado
    return arriesgo