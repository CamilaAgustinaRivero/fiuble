# Rivero, Camila Agustina
"""
Parámetros:
    fecha_partida: la fecha en la que inicio la partida.
    hora_finalizacion: hora en la que termino la partida.
    nombre_jugador: nombre del jugador actual.
    aciertos: número que indica la cantidad de aciertos de cada jugador.
    intentos: número que indica la cantidad de intentos de cada jugador.
    metodo: string (puede ser a o w) que determina si la partida se sobreescribe o no.
Salidas:
    Crea un archivo con la información de cada partida.
"""


def guardar_partidas(fecha_partida, hora_finalizacion, nombre_jugador, aciertos, intentos, metodo):
    try:
        archivo = open("../archivos_generados/partidas.csv", metodo)
    except FileNotFoundError:
        archivo = open("../archivos_generados/partidas.csv", "w")
    linea = "{},{},{},{},{}\n".format(fecha_partida, hora_finalizacion, nombre_jugador, aciertos, intentos)
    archivo.write(linea)
    archivo.close()
