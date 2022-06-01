# Rivero, Camila Agustina
"""
Función: validar_arriesgo
Parámetros:
    arriesgo: cadena que contiene el arriesgo a validar, ingresado por el usuario.
    LONGITUD_PALABRA: número que indica la cantidad de caracteres de la palabra a adivinar.
Salidas:
    Devuelve True si el arriesgo ingresado es válido y False si el arriesgo ingresado es inválido.
"""


def validar_arriesgo(arriesgo, LONGITUD_PALABRA, obtener_color):
    valido = False
    if not arriesgo.isalpha():
        print(obtener_color("Rojo") + "Debe ingresar solo letras." + obtener_color("Defecto") + "\n")
    elif len(arriesgo) != LONGITUD_PALABRA:
        print(obtener_color("Rojo") + "Debe ingresar una palabra de " + str(LONGITUD_PALABRA) + " letras." + obtener_color("Defecto") + "\n")
    else:
        valido = True
    return valido
