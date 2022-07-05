# Gonzalez, Daniel y Salvador, Federico
"""
Función: escoger_modo
Parámetros:
    Esta función no tiene parámetros.
Salidas:
"""
import random

def escoger_modo(modo_juego, usuario_1, usuario_2):
    orden_turnos = False
    PRIMERO = 0
    SEGUNDO = 1
    cola_turnos = ['', '']        

    if modo_juego == '2':
        # Se determina el usuario que inicia la partida
        if not orden_turnos:
                cola_turnos[PRIMERO] = random.choice((usuario_1, usuario_2))
        if cola_turnos[PRIMERO] == usuario_1:
                cola_turnos[SEGUNDO] = usuario_2
        else:
                cola_turnos[SEGUNDO] = usuario_1
        print(f"{cola_turnos[PRIMERO]} juega primero!", end="\n\n")
    else:
        cola_turnos[PRIMERO] = usuario_1
    return cola_turnos, PRIMERO, SEGUNDO
