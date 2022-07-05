import random
from utiles.utiles import obtener_color
from funciones.configuraciones import establecer_configuraciones, configuraciones
from funciones.escoger_modo import escoger_modo
from funciones.leer_archivo import unificar_archivos
from funciones.cronometro import fecha_actual, iniciar_cronometro, detener_cronometro, tiempo_transcurrido
from funciones.actualizar_coincidencias import actualizar_coincidencias
from funciones.normalizar_arriesgo import normalizar_palabra
from funciones.validar_arriesgo import validar_arriesgo
from funciones.presentar import presentar
from funciones.actualizar_puntaje import actualizar_puntaje
from funciones.resultado import resultado
from funciones.continuar_jugando import continuar_jugando
from funciones.guardar_partidas import guardar_partidas


def main(modo_juego, usuario_1, usuario_2=""):
    # Condiciones iniciales del juego
    iniciar_partida = True
    establecer_configuraciones()
    configuracion = configuraciones()
    LONGITUD_PALABRA = configuracion["LONGITUD_PALABRA_SECRETA"][0]
    LIMITE_PARTIDAS = configuracion["MAXIMO_PARTIDAS"][0]
    LIMITE_INTENTOS = 5
    partida = 0
    tabla = {}
    cola_turnos, PRIMERO, SEGUNDO = escoger_modo(modo_juego, usuario_1, usuario_2)
    aciertos_totales1 = aciertos_totales2 = 0
    intentos_totales1 = intentos_totales2 = 0
    diccionario = unificar_archivos(LONGITUD_PALABRA)
    fecha = fecha_actual()
    tiempo_fin = 0

    while iniciar_partida and partida < LIMITE_PARTIDAS:
        # Condiciones iniciales de cada partida
        palabra_a_adivinar = random.choice(list(diccionario)).upper()
        print(palabra_a_adivinar)
        intentos = 0
        arriesgo = ""
        coincidencias = []
        tiempo_inicio = iniciar_cronometro()

        # La lista coincidencias tiene una longitud dinámica
        for incognita in range(LONGITUD_PALABRA):
            coincidencias.append("?")
        coincidencias_parciales = []

        # Validación de arriesgos e intentos durante cada partida
        while intentos <= LIMITE_INTENTOS and arriesgo != palabra_a_adivinar:
            actualizar_coincidencias(LIMITE_INTENTOS, coincidencias_parciales, LONGITUD_PALABRA)
            if intentos < LIMITE_INTENTOS:
                arriesgo = normalizar_palabra(input(f"{cola_turnos[PRIMERO]}, tu arriesgo: ").upper())
                arriesgo_valido = validar_arriesgo(arriesgo, LONGITUD_PALABRA, obtener_color)
                if arriesgo_valido:
                    resultado_parcial, coincidencias = presentar(palabra_a_adivinar, arriesgo, obtener_color, coincidencias)
                    coincidencias_parciales.append(resultado_parcial)
                    print(f"{resultado_parcial}\n")
                    if modo_juego == '2' and arriesgo != palabra_a_adivinar and intentos != LIMITE_INTENTOS - 1:
                        # Cambio de turno agregando nombre del jugador actual y removiendolo del primer lugar
                        cola_turnos.append(cola_turnos[PRIMERO])
                        cola_turnos.pop(PRIMERO)
                    intentos += 1
                print(f"Palabra a adivinar: {' '.join(coincidencias)}")
            else:
                print(f"Palabra a adivinar: {palabra_a_adivinar}")
                intentos += 1

        tabla, puntos = actualizar_puntaje(tabla, intentos, cola_turnos[0], cola_turnos[1])
        tiempo_fin = detener_cronometro()
        tiempo = tiempo_transcurrido(tiempo_inicio, tiempo_fin)
        acertado = resultado(arriesgo, palabra_a_adivinar, modo_juego, tiempo)
        if acertado and cola_turnos[0]==PRIMERO:
            aciertos_totales1 += 1
        elif acertado:
            aciertos_totales2 += 1
        print(f"{cola_turnos[PRIMERO]}, obtuviste {puntos} puntos. Tenes acumulados {tabla.get(cola_turnos[PRIMERO])} puntos en total.")
        if modo_juego == '2':
            print(f"{cola_turnos[SEGUNDO]}, obtuviste {-puntos} puntos. Tenes acumulados {tabla.get(cola_turnos[SEGUNDO])} puntos en total." if puntos != -100 else f"{cola_turnos[SEGUNDO]}, obtuviste {int(puntos/2)} puntos. Tenes acumulados {tabla.get(cola_turnos[SEGUNDO])} puntos en total.")
        partida += 1
        if partida < LIMITE_PARTIDAS:
            iniciar_partida, cola_turnos = continuar_jugando(modo_juego, cola_turnos, tabla, PRIMERO, iniciar_partida)
    
    # Cuando se termina de jugar todas las partidas
    guardar_partidas(fecha, tiempo_fin, cola_turnos[PRIMERO], aciertos_totales1, intentos_totales1)
    if modo_juego == '2':
        guardar_partidas(fecha, tiempo_fin, cola_turnos[SEGUNDO], aciertos_totales2, intentos_totales2)
