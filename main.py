import random
from unidecode import unidecode
from utiles import obtener_palabras_validas, obtener_color
from funciones.cronometro import iniciar_cronometro, detener_cronometro
from funciones.actualizar_puntaje import actualizar_puntaje
from funciones.resultado import resultado
from funciones.escoger_modo import escoger_modo
from funciones.continuar_jugando import continuar_jugando
from funciones.actualizar_coincidencias import actualizar_coincidencias
from funciones.validar_arriesgo import validar_arriesgo
from funciones.presentar import presentar


def main():
    iniciar_partida = True
    LIMITE_INTENTOS = 5
    tabla = {}
    
    cola_turnos, PRIMERO, SEGUNDO, modo_juego = escoger_modo()

    while iniciar_partida:
        # Condiciones iniciales de cada partida
        PALABRA_A_ADIVINAR = random.choice(obtener_palabras_validas()).upper()
        print(PALABRA_A_ADIVINAR)
        LONGITUD_PALABRA = len(PALABRA_A_ADIVINAR)
        intentos = 0
        arriesgo = ""
        coincidencias = []

        tiempo_inicio = iniciar_cronometro()

        # La lista coincidencias tiene una longitud dinámica
        for incognita in range(LONGITUD_PALABRA):
            coincidencias.append("?")
        coincidencias_parciales = []

        # Validación de arriesgos e intentos durante cada partida
        
        while intentos <= LIMITE_INTENTOS and arriesgo != PALABRA_A_ADIVINAR:
            actualizar_coincidencias(LIMITE_INTENTOS, coincidencias_parciales, LONGITUD_PALABRA)
            if intentos < LIMITE_INTENTOS:
                arriesgo = unidecode(input(f"{cola_turnos[PRIMERO]}, tu arriesgo: ").upper(), "utf-8")
                arriesgo_valido = validar_arriesgo(arriesgo, LONGITUD_PALABRA, obtener_color)
                if arriesgo_valido:
                    resultado_parcial, coincidencias = presentar(PALABRA_A_ADIVINAR, arriesgo, obtener_color, coincidencias)
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

        tabla, puntos = actualizar_puntaje(tabla, intentos, cola_turnos[0], cola_turnos[1])
        tiempo_final = detener_cronometro(tiempo_inicio)
        resultado(arriesgo, PALABRA_A_ADIVINAR, modo_juego, tiempo_final)
        print(f"{cola_turnos[PRIMERO]}, obtuviste {puntos} puntos. Tenes acumulados {tabla.get(cola_turnos[PRIMERO])} puntos en total.")
        print(f"{cola_turnos[SEGUNDO]}, obtuviste {puntos} puntos. Tenes acumulados {tabla.get(cola_turnos[SEGUNDO])} puntos en total." if modo_juego == '2' else '')

        iniciar_partida, cola_turnos = continuar_jugando(modo_juego, cola_turnos, tabla, PRIMERO, iniciar_partida)

main()
