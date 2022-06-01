# Rivero, Camila Agustina
"""
Función: validar_indice
Parámetros:
    LIMITE_INTENTOS: número que indica la cantidad de intentos posible.
    coincidencias_parciales: lista que contiene las coincidencias encontradas en cada arriesgo válido.
    LONGITUD_PALABRA: número que indica la cantidad de caracteres de la palabra a adivinar.
Salidas:
    Imprime en pantalla las coincidencias encontradas luego de ingresar un arriesgo válido y las incógnitas restantes.
"""


def actualizar_coincidencias(LIMITE_INTENTOS, coincidencias_parciales, LONGITUD_PALABRA):
    for i in range(LIMITE_INTENTOS):
        try:
            print(coincidencias_parciales[i])
        except IndexError:
            print("? " * LONGITUD_PALABRA)
