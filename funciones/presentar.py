# Apellido, Nombre
"""
Función: presentar
Parámetros:
    PALABRA_A_ADIVINAR: cadena que contiene la palabra a adivinar.
    arriesgo: cadena que contiene un arriesgo válido ingresado por el usuario.
    obtener_color: función que obtiene los colores de utiles.py
Salidas:
    Devuelve las letras del arriesgo coloreadas con sus colores correspondientes y una lista con el arriesgo ingresado.
"""


# Utilizar formato f-strings en los prints para respetar PEP
# Colorear solo una letra cuando aparece dos veces en arriesgo_valido pero solo una en PALABRA_A_ADIVINAR
# Ejemplo: arriesgo_valido = CASAS y PALABRA_A_ADIVINAR = CAMPO -> (muestra dos A amarillas y deberia mostrar solo una)
def presentar(PALABRA_A_ADIVINAR, arriesgo, obtener_color, coincidencias):
    resultado = ""
    for pos in range(len(arriesgo)):
        letra = arriesgo[pos]
        if letra == PALABRA_A_ADIVINAR[pos]:
            resultado += obtener_color("Verde") + letra + " " + obtener_color("Defecto")
            coincidencias[pos] = letra
        elif letra in PALABRA_A_ADIVINAR:
            resultado += obtener_color("Amarillo") + letra + " " + obtener_color("Defecto")
        else:
            resultado += obtener_color("GrisOscuro") + letra + " " + obtener_color("Defecto")
    return resultado + obtener_color("Defecto"), coincidencias
