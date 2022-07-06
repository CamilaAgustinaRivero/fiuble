# Rivero, Camila Agustina
"""
Parámetros:
    Esta función no tiene parámetros.
Salidas:
    .
"""


def guardar_partidas(fecha_partida, hora_finalizacion, nombre_jugador, aciertos, intentos, metodo):
    try:
        archivo = open("../archivos_generados/partidas.csv", metodo)
    except FileNotFoundError:
        archivo = open("../archivos_generados/partidas.csv", "w")
    linea = "{},{},{},{},{}\n".format(fecha_partida, hora_finalizacion, nombre_jugador, aciertos, intentos)
    archivo.write(linea)
    archivo.close()
