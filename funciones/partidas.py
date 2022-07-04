# Rivero, Camila Agustina
"""
Parámetros:
    Esta función no tiene parámetros.
Salidas:
    .
"""


def guardar_partidas():
    try:
        archivo = open("./partidas.csv", "r+")
        print("archivo abrido xd")
        archivo.close()
    except FileNotFoundError:
        archivo = open("./partidas.csv", "w")
        print("archivo creado")
