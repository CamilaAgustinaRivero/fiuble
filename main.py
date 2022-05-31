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
    LIMITE_INTENTOS = 5
    modo_juego = 0
    usuario_2 = ""
    tabla = {}

    # No sale del ciclo hasta seleccionar un modo válido
    while modo_juego not in ['1', '2']:
        modo_juego = input("Introduzca 1 para jugar modo individual o 2 para modo 2 jugadores: ")

    if modo_juego == '1':
        usuario_1 = input("Usuario 1: Ingrese su nombre para empezar a jugar: ").capitalize()
    else:
        nombre_usuario_1 = input("Usuario 1: Ingrese su nombre para empezar a jugar: ").capitalize()
        nombre_usuario_2 = input("Usuario 2: Ingrese su nombre: ").capitalize()
        # Se determina el usuario que inicia la partida
        usuario_1 = random.choice((nombre_usuario_1, nombre_usuario_2))
        if usuario_1 == nombre_usuario_1:
            usuario_2 = nombre_usuario_2
        else:
            usuario_2 = nombre_usuario_1

    while iniciar_partida:
        # Condiciones iniciales de cada partida
        PALABRA_A_ADIVINAR = random.choice(obtener_palabras_validas()).upper()
        LONGITUD_PALABRA = len(PALABRA_A_ADIVINAR)
        print(PALABRA_A_ADIVINAR)
        primer_turno = usuario_1
        segundo_turno = usuario_2
        intentos = 0
        arriesgo = ""
        coincidencias = []
        # La lista coincidencias tiene una longitud dinámica
        for incognita in range(LONGITUD_PALABRA):
            coincidencias.append("?")
        coincidencias_parciales = []

        print(f"{usuario_1} juega primero!", end="\n\n")

        tiempo_inicio = iniciar_cronometro()
        # Validación de arriesgos e intentos durante cada partida
        while intentos <= LIMITE_INTENTOS and arriesgo != PALABRA_A_ADIVINAR:
            actualizar_coincidencias(LIMITE_INTENTOS, coincidencias_parciales, LONGITUD_PALABRA)
            if intentos < LIMITE_INTENTOS:
                arriesgo = unidecode(input(f"{usuario_1}, tu arriesgo: ").upper(), "utf-8")
                arriesgo_valido = validar_arriesgo(arriesgo, LONGITUD_PALABRA, obtener_color)
                if arriesgo_valido:
                    resultado_parcial, coincidencias = presentar(PALABRA_A_ADIVINAR, arriesgo, obtener_color, coincidencias)
                    coincidencias_parciales.append(resultado_parcial)
                    print(f"{resultado_parcial}\n")
                    if modo_juego == '2' and arriesgo != PALABRA_A_ADIVINAR:
                        # Cambio de turno actual usando desenpaquetamiento
                        usuario_1, usuario_2 = usuario_2, usuario_1
                    intentos += 1
                print(f"Palabra a adivinar: {' '.join(coincidencias)}")
            else:
                print(f"Palabra a adivinar: {PALABRA_A_ADIVINAR}")
                intentos += 1
        if intentos == 5:
            usuario_1, usuario_2 = usuario_2, usuario_1
        ronda = actualizar_puntaje(intentos, tabla, usuario_1, usuario_2)
        tabla = ronda[0]
        puntos = ronda[1]
        tiempo_final = detener_cronometro(tiempo_inicio)
        resultado(arriesgo, PALABRA_A_ADIVINAR, modo_juego, tiempo_final)
        print(f"{usuario_1}, obtuviste {puntos} puntos. Tenes acumulados {tabla.get(usuario_1)} puntos en total.")
        print(f"{usuario_2}, perdiste. Tenes acumulados {tabla.get(usuario_2)} puntos en total." if usuario_2 != '' else '')

        # Continuar jugando ?
        continuar = unidecode(input("¿Continuar jugando? - S/N: ").upper(), "utf-8")
        if continuar == "S":
            if modo_juego == "2":
                usuario_1, usuario_2 = segundo_turno, primer_turno
        elif continuar == "N":
            iniciar_partida = False
        else:
            print("Opción incorrecta.")


main()
