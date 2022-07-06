# Apellido, Nombre
"""
Función: resultado
Parámetros:
    arriesgo:
    palabra_a_adivinar:
    modo_juego:
    obtener_tiempo_jugador:
Salidas:
    Imprime en pantalla un mensaje indicando si se perdió o ganó la partida.
"""


def resultado(arriesgo, palabra_a_adivinar, modo_juego, tiempo):
    acertado = arriesgo == palabra_a_adivinar
    if modo_juego == '1':
        if acertado:
            print(f"Ganaste! Tardaste {tiempo} en adivinar la palabra.")
        else:
            print("Perdiste!")
    else:
        if acertado:
            print(f"La palabra fue adivinada en {tiempo}.")
        else:
            print("Perdieron!")
    return acertado
