# Apellido, Nombre
"""
Función: resultado
Parámetros:
    arriesgo:
    PALABRA_A_ADIVINAR:
    modo_juego:
    obtener_tiempo_jugador:
Salidas:
    Imprime en pantalla un mensaje indicando si se perdió o ganó la partida.
"""


def resultado(arriesgo, PALABRA_A_ADIVINAR, modo_juego, tiempo_final):
    if modo_juego == '1':
        if arriesgo == PALABRA_A_ADIVINAR:
            print(f"Ganaste! Tardaste {tiempo_final} en adivinar la palabra.")
        else:
            print("Perdiste!")
    else:
        if arriesgo == PALABRA_A_ADIVINAR:
            print(f"La palabra fue adivinada en {tiempo_final}.")
        else:
            print("Perdieron!")
