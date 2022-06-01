# Fonzalez, Daniel
"""
Función: presentar
Parámetros:
    PALABRA_A_ADIVINAR: cadena que contiene la palabra a adivinar.
    arriesgo: cadena que contiene un arriesgo válido ingresado por el usuario.
    obtener_color: función que obtiene los colores de utiles.py
Salidas:
    Devuelve las letras del arriesgo coloreadas con sus colores correspondientes y una lista con el arriesgo ingresado.
"""


def presentar(PALABRA_A_ADIVINAR, arriesgo, obtener_color, coincidencias):
    resultado = ""
    datos_coincidencias = {}
    
    #Inicializa el diccionario con todas las letras en 0
    for i in range(len(arriesgo)):
        datos_coincidencias[arriesgo[i]] = 0
    
    #Busca primero todas las coincidencias y a su vez las cantidades encontradas
    for pos in range(len(arriesgo)):
        letra = arriesgo[pos]
        if letra == PALABRA_A_ADIVINAR[pos]:
            coincidencias[pos] = letra
            datos_coincidencias[letra] += 1
    
    #Tomando en cuenta las coincidencias ya encontradas pinta los colores correspondientes
    for posicion in range(len(arriesgo)):
        letra2 = arriesgo[posicion]
        
        if letra2 == PALABRA_A_ADIVINAR[posicion]:
            resultado += obtener_color ("Verde") + letra2 + " " +obtener_color ("Defecto")
        elif(letra2 in PALABRA_A_ADIVINAR and letra2 not in arriesgo[0:posicion] and PALABRA_A_ADIVINAR.count(letra2) > datos_coincidencias[letra2]):
            resultado += obtener_color ("Amarillo") + letra2 + " " + obtener_color ("Defecto")
        else:
            resultado += obtener_color ("Defecto") + letra2 + " " +obtener_color ("Defecto")
        
    return resultado + obtener_color ("Defecto"), coincidencias
