# Federico Salvador
"""
Función: normalizar_palabra
Parámetros:
    arriesgo: cadena de caracteres que contiene un arriesgo ingresado por el usuario.
Salidas:
    Detecta si la palabra no forma parte de los primeros 128 caracteres de ASCII y devuelve la palabra ingresada sin tildes, si las contiene,
    para su procesamiento en el programa.
"""


def normalizar_palabra(arriesgo):
    if arriesgo.isalpha() and not arriesgo.isascii():
        resultado = ''
        vocales_tildadas = ['Á', 'É', 'Í', 'Ó', 'Ú']
        for caracter in arriesgo:
            if caracter in vocales_tildadas:
                if caracter == 'Á':
                    resultado += 'A'
                elif caracter == 'É':
                    resultado += 'E'
                elif caracter == 'Í':
                    resultado += 'I'
                elif caracter == 'Ó':
                    resultado += 'O'
                else:
                    resultado += 'U'
            else:
                resultado += caracter

        arriesgo = resultado

    return arriesgo
