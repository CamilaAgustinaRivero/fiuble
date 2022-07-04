# Rivero, Camila Agustina
"""
Función:
Parámetros:
    Esta función no tiene parámetros.
Salidas:
"""


def establecer_configuraciones():
    pass


"""
Función: configuraciones
Parámetros:
    Esta función no tiene parámetros.
Salidas:
    Retorna un diccionario con la configuración del juego.
"""


def configuraciones():
    tipo_configuracion = "VALOR POR DEFECTO"
    configuracion = {
        "LONGITUD_PALABRA_SECRETA": (5, tipo_configuracion),
        "MAXIMO_PARTIDAS": (5, tipo_configuracion),
        "MAXIMO_INTENTOS": (5, tipo_configuracion),
        "REINICIAR_ARCHIVO_PARTIDAS": (False, tipo_configuracion)
    }
    try:
        tipo_configuracion = "VALOR CONFIGURADO CORRECTAMENTE"
        archivo = open("./configuracion.csv", "r")
        for linea in archivo:
            clave, valor = linea.strip("\n").split(",")
            if clave in configuracion:
                if valor.isdecimal():
                    configuracion[clave] = (int(valor), tipo_configuracion)
                else:
                    configuracion[clave] = (valor, tipo_configuracion)
        archivo.close()
    except FileNotFoundError:
        print(f"Error al procesar archivo de configuración.")
    
    for elemento in configuracion:
        print(f"{elemento}: {configuracion[elemento][0]} - {configuracion[elemento][1]}")
    print("\n")
    return configuracion
