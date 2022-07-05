import random
from funciones.configuraciones import configuraciones
from funciones.normalizar_arriesgo import normalizar_palabra
from funciones.cronometro import iniciar_cronometro, detener_cronometro, tiempo_transcurrido
from funciones.actualizar_puntaje import actualizar_puntaje
from funciones.resultado import resultado
from funciones.escoger_modo import escoger_modo
from funciones.continuar_jugando import continuar_jugando
from funciones.actualizar_coincidencias import actualizar_coincidencias
from funciones.validar_arriesgo import validar_arriesgo
from funciones.presentar import presentar
from funciones.guardar import guardar
from funciones.leer_archivo import leer_archivo
from funciones.guardar_partidas import guardar_partidas
from utiles import obtener_color


def main():
    iniciar_partida = True
    configuracion = configuraciones()
    LIMITE_INTENTOS = configuracion["MAXIMO_INTENTOS"][0]
    LIMITE_PARTIDAS = configuracion["MAXIMO_PARTIDAS"][0]
    LONGITUD_PALABRA = configuracion["LONGITUD_PALABRA_SECRETA"][0]
    partida = 0
    tabla = {}
    cola_turnos, PRIMERO, SEGUNDO, modo_juego = escoger_modo()
    
    with open("Cuentos.txt", "r") as archivo_entrada1, open("La araña negra - tomo 1.txt", "r") as archivo_entrada2, open(
        "Las 1000 Noches y 1 Noche.txt", "r") as archivo_entrada3, open("palabras.csv", "w") as archivo_salida:
        archivos = [archivo_entrada1, archivo_entrada2, archivo_entrada3]
        i = 0
        dic_desordenado = {}
        for archivo in archivos:
            diccionario = leer_archivo (archivo, dic_desordenado, i, LONGITUD_PALABRA)
            i += 1
        guardar(diccionario, archivo_salida)
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
        resultado(arriesgo, palabra_a_adivinar, modo_juego, tiempo)
        print(f"{cola_turnos[PRIMERO]}, obtuviste {puntos} puntos. Tenes acumulados {tabla.get(cola_turnos[PRIMERO])} puntos en total.")
        guardar_partidas(tiempo_inicio, tiempo_fin, cola_turnos[PRIMERO], "aciertos", "intentos")
        if modo_juego == '2':
            print(f"{cola_turnos[SEGUNDO]}, obtuviste {-puntos} puntos. Tenes acumulados {tabla.get(cola_turnos[SEGUNDO])} puntos en total." if puntos != -100 else f"{cola_turnos[SEGUNDO]}, obtuviste {int(puntos/2)} puntos. Tenes acumulados {tabla.get(cola_turnos[SEGUNDO])} puntos en total.")
            guardar_partidas(tiempo_inicio, tiempo_fin, cola_turnos[SEGUNDO], "aciertos", "intentos")
        partida += 1
        if partida < LIMITE_PARTIDAS:
            iniciar_partida, cola_turnos = continuar_jugando(modo_juego, cola_turnos, tabla, PRIMERO, iniciar_partida)

main()
