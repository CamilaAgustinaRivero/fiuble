# Nombre, Apellido

"""
Función: continuar_jugando
Parámetros:
    modo_juego:
    cola_turnos:
    tabla:
    PRIMERO:
    iniciar_partida:
Salidas:
"""


def continuar_jugando(modo_juego, cola_turnos, tabla, PRIMERO, iniciar_partida):
    # Continuar jugando ?
    continuar = ''
    while continuar not in ['S', 'N']:
        continuar = input("¿Desea jugar otra partida? (S/N): ").upper()
    if continuar == "S":
        if modo_juego == '2':
            cola_turnos.append(cola_turnos[PRIMERO])
            cola_turnos.pop(PRIMERO)
    else:
        iniciar_partida = False
        if modo_juego == '2':
            ganador = sorted(tabla.items(), key=lambda x: x[1], reverse=True)
            if ganador[0][1] == ganador[1][1]:
                print("Empate!")
            else:
                print(f"El ganador es {ganador[0][0]}, con un total de {ganador[0][1]} puntos.")
    return iniciar_partida, cola_turnos
