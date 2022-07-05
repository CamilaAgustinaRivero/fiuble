# Rivero, Camila Agustina
"""
Parámetros:
    Esta función no tiene parámetros.
Salidas:
    .
"""


def guardar_partidas(fecha_partida, hora_finalizacion, nombre_jugador, aciertos, intentos):
    try:
        archivo = open("archivos/partidas.csv", "a")
    except FileNotFoundError:
        archivo = open("archivos/partidas.csv", "w")
    linea = "{},{},{},{},{}\n".format(fecha_partida, hora_finalizacion, nombre_jugador, aciertos, intentos)
    archivo.write(linea)
    archivo.close()
    