import random
from unidecode import unidecode
from utiles import obtener_palabras_validas
from utiles import obtener_color
from funciones.cronometro import iniciar_cronometro, detener_cronometro
from funciones.actualizar_coincidencias import actualizar_coincidencias
from funciones.validar_arriesgo import validar_arriesgo
from funciones.presentar import presentar
from funciones.actualizar_puntaje import actualizar_puntaje
from funciones.resultado import resultado


def main():
    iniciar_partida = True
    orden_turnos = False
    LIMITE_INTENTOS = 5
    PRIMERO = 0
    SEGUNDO = 1
    modo_juego = 0
    cola_turnos = ['', '']
    tabla = {}

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

    while iniciar_partida:
        # Condiciones iniciales de cada partida
        PALABRA_A_ADIVINAR = random.choice(obtener_palabras_validas()).upper()
        LONGITUD_PALABRA = len(PALABRA_A_ADIVINAR)
        intentos = 0
        arriesgo = ""
        coincidencias = []
        # La lista coincidencias tiene una longitud dinámica
        for incognita in range(LONGITUD_PALABRA):
            coincidencias.append("?")
        coincidencias_parciales = []

        tiempo_inicio = iniciar_cronometro()
        # Validación de arriesgos e intentos durante cada partida
        while intentos <= LIMITE_INTENTOS and arriesgo != PALABRA_A_ADIVINAR:
            actualizar_coincidencias(LIMITE_INTENTOS, coincidencias_parciales, LONGITUD_PALABRA)
            if intentos < LIMITE_INTENTOS:
                arriesgo = unidecode(input(f"{cola_turnos[PRIMERO]}, tu arriesgo: ").upper(), "utf-8")
                arriesgo_valido = validar_arriesgo(arriesgo, LONGITUD_PALABRA, obtener_color)
                if arriesgo_valido:
                    resultado_parcial, coincidencias = presentar(PALABRA_A_ADIVINAR, arriesgo, obtener_color,
                                                                 coincidencias)
                    coincidencias_parciales.append(resultado_parcial)
                    print(f"{resultado_parcial}\n")
                    if modo_juego == '2' and arriesgo != PALABRA_A_ADIVINAR and intentos != LIMITE_INTENTOS - 1:
                        # Cambio de turno agregando nombre del jugador actual y removiendolo del primer lugar
                        cola_turnos.append(cola_turnos[PRIMERO])
                        cola_turnos.pop(PRIMERO)
                    intentos += 1
                print(f"Palabra a adivinar: {' '.join(coincidencias)}")
            else:
                print(f"Palabra a adivinar: {PALABRA_A_ADIVINAR}")
                intentos += 1
        tabla, puntos = actualizar_puntaje(intentos, tabla, cola_turnos[0], cola_turnos[1])
        tiempo_final = detener_cronometro(tiempo_inicio)
        resultado(arriesgo, PALABRA_A_ADIVINAR, modo_juego, tiempo_final)
        print(f"{cola_turnos[PRIMERO]}, obtuviste {puntos} puntos. Tenes acumulados {tabla.get(cola_turnos[PRIMERO])} puntos en total.")
        print(f"{cola_turnos[SEGUNDO]}, obtuviste {puntos} puntos. Tenes acumulados {tabla.get(cola_turnos[SEGUNDO])} puntos en total." if modo_juego == '2' else '')

        # Continuar jugando ?
        continuar = unidecode(input("¿Desea jugar otra partida? (S/N): ").upper(), "utf-8")
        if continuar == "S":
            if modo_juego == "2":
                cola_turnos.append(cola_turnos[PRIMERO])
                cola_turnos.pop(PRIMERO)
        elif continuar == "N":
            iniciar_partida = False
            if modo_juego == '2':
                ganador = sorted(tabla.items(), key=lambda p: p)
                if ganador[0][1] == ganador[1][1]:
                    print("Empate!")
                else:
                    print(f"El ganador es {ganador[0][0]}, con un total de {ganador[0][1]} puntos.")
        else:
            print("Opción incorrecta.")


main()
