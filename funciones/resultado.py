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


def resultado(arriesgo, palabra_a_adivinar, modo_juego, tiempo_final):
    if modo_juego == '1':
        if arriesgo == palabra_a_adivinar:
            print(f"Ganaste! Tardaste {tiempo_final} en adivinar la palabra.")
        else:
            print("Perdiste!")
    else:
        if arriesgo == palabra_a_adivinar:
            print(f"La palabra fue adivinada en {tiempo_final}.")
        else:
            print("Perdieron!")
