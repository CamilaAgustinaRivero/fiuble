# Villafañez, German Dario
from datetime import *
import time

"""
Función: iniciar_cronometro
Parámetros:
Salidas:
"""


def iniciar_cronometro():
    tiempo_inicio = str(datetime.now().hour) + ":" + str(datetime.now().minute) + ":" + str(datetime.now().second)
    return tiempo_inicio


"""
Función: detener_cronometro
Parámetros:
    tiempo_inicio:
Salidas:
    Devuelve una cadena con el tiempo transcurrido en minutos y segundos.
"""


def detener_cronometro(tiempo_inicio):
    tiempo_fin = str(datetime.now().hour) + ":" + str(datetime.now().minute) + ":" + str(datetime.now().second)
    tiempo_transcurrido = datetime.strptime(tiempo_fin, "%H:%M:%S") - datetime.strptime(tiempo_inicio, "%H:%M:%S")
    minutos_transcurridos = int(time.strftime("%M", time.gmtime(tiempo_transcurrido.seconds)))
    segundos_transurridos = int(time.strftime("%S", time.gmtime(tiempo_transcurrido.seconds)))
    return "{0} minutos y {1} segundos".format(minutos_transcurridos, segundos_transurridos)
