# Rivero, Camila Agustina
"""
Parámetros:
    Esta función no tiene parámetros.
Salidas:
    .
"""


def guardar_partidas(fecha_partida, hora_finalizacion, nombre_jugador, aciertos, intentos):
    try:
        archivo = open("./partidas.csv", "a")
    except FileNotFoundError:
        archivo = open("./partidas.csv", "w")
    linea = "{},{},{},{},{}\n".format(fecha_partida, hora_finalizacion, nombre_jugador, aciertos, intentos)
    archivo.write(linea)
    archivo.close()
    