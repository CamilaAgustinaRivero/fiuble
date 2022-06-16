import random

def escoger_modo():
    orden_turnos = False
    PRIMERO = 0
    SEGUNDO = 1
    modo_juego = 0
    cola_turnos = ['', '']

    # No sale del ciclo hasta seleccionar un modo válido
    while modo_juego not in ['1', '2']:
        modo_juego = input("Introduzca 1 para jugar modo individual o 2 para modo 2 jugadores: ")

        usuario_1 = input("Usuario 1: Ingrese su nombre para empezar a jugar: ").capitalize()
        cola_turnos[PRIMERO] = usuario_1

        if modo_juego == '2':
            usuario_2 = input("Usuario 2: Ingrese su nombre: ").capitalize()
            # Se determina el usuario que inicia la partida
            if not orden_turnos:
                cola_turnos[PRIMERO] = random.choice((usuario_1, usuario_2))

            if cola_turnos[PRIMERO] == usuario_1:
                cola_turnos[SEGUNDO] = usuario_2
            else:
                cola_turnos[SEGUNDO] = usuario_1
            print(f"{cola_turnos[PRIMERO]} juega primero!", end="\n\n")
    return cola_turnos, PRIMERO, SEGUNDO, modo_juego
