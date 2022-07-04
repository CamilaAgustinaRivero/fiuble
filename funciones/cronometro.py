# Villafañez, German Dario
from datetime import *
import time

"""
Función: iniciar_cronometro
Parámetros:
    No tiene parametros.
Salidas:
    Retorna el tiempo de inicio de la partida.
"""


def iniciar_cronometro():
    tiempo_inicio = str(datetime.now().hour) + ":" + str(datetime.now().minute) + ":" + str(datetime.now().second)
    return tiempo_inicio


"""
Función: iniciar_cronometro
Parámetros:
    No tiene parametros.
Salidas:
    Retorna el tiempo de finalización de la partida.
"""


def detener_cronometro():
    tiempo_fin = str(datetime.now().hour) + ":" + str(datetime.now().minute) + ":" + str(datetime.now().second)
    return tiempo_fin


"""
Función: detener_cronometro
Parámetros:
    tiempo_inicio: indica el momento en el cual inició la partida.
    tiempo_fin: indica el momento en el cual finalizó la partida.
Salidas:
    Devuelve una cadena con el tiempo transcurrido en minutos y segundos.
"""


def tiempo_transcurrido(tiempo_inicio, tiempo_fin):
    tiempo_transcurrido = datetime.strptime(tiempo_fin, "%H:%M:%S") - datetime.strptime(tiempo_inicio, "%H:%M:%S")
    minutos_transcurridos = int(time.strftime("%M", time.gmtime(tiempo_transcurrido.seconds)))
    segundos_transurridos = int(time.strftime("%S", time.gmtime(tiempo_transcurrido.seconds)))
    return "{0} minutos y {1} segundos".format(minutos_transcurridos, segundos_transurridos)
