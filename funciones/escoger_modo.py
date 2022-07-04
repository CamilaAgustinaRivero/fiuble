# Fonzalez, Daniel y Salvador, Federico
"""
Función: presentar
Parámetros:
    PALABRA_A_ADIVINAR: cadena que contiene la palabra a adivinar.
    arriesgo: cadena que contiene un arriesgo válido ingresado por el usuario.
    obtener_color: función que obtiene los colores de utiles.py
    coincidencias:
Salidas:
    Devuelve las letras del arriesgo coloreadas con sus colores correspondientes y una lista con el arriesgo ingresado.
"""

import random

def validar_usuarios(usuario, lista_usuarios):
    lista_usuarios.append(usuario)
    while usuario == '':
        usuario = input(f"Ingrese un nombre válido para empezar a jugar: ").capitalize()
        while (len(lista_usuarios) == 2 and lista_usuarios[0] == lista_usuarios[1]):
            usuario = input(f"Ingrese un nombre válido para empezar a jugar: ").capitalize()
            lista_usuarios[1] = usuario
    return usuario


def escoger_modo():
    orden_turnos = False
    PRIMERO = modo_juego = 0
    SEGUNDO = 1
    INDIVIDUAL = '1'
    MULTIJUGADOR = '2'
    cola_turnos = ['', '']
    lista_usuarios = []

    # No sale del ciclo hasta seleccionar un modo válido
    while modo_juego not in [INDIVIDUAL, MULTIJUGADOR]:
        modo_juego = input("Introduzca 1 para jugar modo individual o 2 para modo multijugador (2 jugadores): ")

        usuario_1 = input("Usuario 1: Ingrese su nombre para empezar a jugar: ").capitalize()
        usuario_1 = validar_usuarios(usuario_1, lista_usuarios)
        cola_turnos[PRIMERO] = usuario_1

        if modo_juego == MULTIJUGADOR:
            usuario_2 = input("Usuario 2: Ingrese su nombre: ").capitalize()
            usuario_2 = validar_usuarios(usuario_2, lista_usuarios)
            # Se determina el usuario que inicia la partida
            if not orden_turnos:
                cola_turnos[PRIMERO] = random.choice((usuario_1, usuario_2))

            if cola_turnos[PRIMERO] == usuario_1:
                cola_turnos[SEGUNDO] = usuario_2
            else:
                cola_turnos[SEGUNDO] = usuario_1
            print(f"{cola_turnos[PRIMERO]} juega primero!", end="\n\n")
    return cola_turnos, PRIMERO, SEGUNDO, modo_juego
