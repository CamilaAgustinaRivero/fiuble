# Rivero, Camila Agustina
"""
Función:
Parámetros:
    Esta función no tiene parámetros.
Salidas:
"""


def establecer_configuraciones():
    mensaje = "Opción incorrecta."
    archivo = open("./configuracion.csv", "w")
    LONGITUD_PALABRA_SECRETA = input("Ingrese la longitud de la palabra: ")
    if LONGITUD_PALABRA_SECRETA.isdecimal():
        linea = "{},{}\n".format('LONGITUD_PALABRA_SECRETA', LONGITUD_PALABRA_SECRETA)
        archivo.write(linea)
    else:
        print(mensaje)

    MAXIMO_PARTIDAS = input("Ingrese el máximo de partidas permitidas: ")
    if MAXIMO_PARTIDAS.isdecimal():
        linea = "{},{}\n".format('MAXIMO_PARTIDAS', MAXIMO_PARTIDAS)
        archivo.write(linea)
    else:
        print(mensaje)

    MAXIMO_INTENTOS = input("Ingrese el máximo de intentos permitidos: ")
    if MAXIMO_INTENTOS.isdecimal():
        linea = "{},{}\n".format('MAXIMO_INTENTOS', MAXIMO_INTENTOS)
        archivo.write(linea)
    else:
        print(mensaje)

    REINICIAR_ARCHIVO_PARTIDAS = input("¿Reiniciar el archivo de partidas? - S/N: ").upper()
    if REINICIAR_ARCHIVO_PARTIDAS == "S":
        REINICIAR_ARCHIVO_PARTIDAS = True
        linea = "{},{}\n".format('REINICIAR_ARCHIVO_PARTIDAS', REINICIAR_ARCHIVO_PARTIDAS)
        archivo.write(linea)
        # borrar partidas guardadas
    elif REINICIAR_ARCHIVO_PARTIDAS == "N":
        REINICIAR_ARCHIVO_PARTIDAS = False
        linea = "{},{}\n".format('REINICIAR_ARCHIVO_PARTIDAS', REINICIAR_ARCHIVO_PARTIDAS)
        archivo.write(linea)
    else:
        print(mensaje)
    archivo.close()


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
