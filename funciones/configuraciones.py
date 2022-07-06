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
    longitud_palabra_secreta = input("Ingrese la longitud de la palabra (entre 3 y 18 caracteres): ")
    if longitud_palabra_secreta.isdecimal() and 3 <= int(longitud_palabra_secreta) <= 18:
        linea = "{},{}\n".format('LONGITUD_PALABRA_SECRETA', longitud_palabra_secreta)
        archivo.write(linea)
    else:
        print(mensaje)

    maximo_partidas = input("Ingrese el máximo de partidas permitidas: ")
    if maximo_partidas.isdecimal() and int(maximo_partidas) >= 1:
        linea = "{},{}\n".format('MAXIMO_PARTIDAS', maximo_partidas)
        archivo.write(linea)
    else:
        print(mensaje)

    reiniciar_archivo_partidas = input("¿Reiniciar el archivo de partidas? - S/N: ").upper()
    if reiniciar_archivo_partidas == "S":
        reiniciar_archivo_partidas = True
        linea = "{},{}\n".format('REINICIAR_ARCHIVO_PARTIDAS', reiniciar_archivo_partidas)
        archivo.write(linea)
    elif reiniciar_archivo_partidas == "N":
        reiniciar_archivo_partidas = False
        linea = "{},{}\n".format('REINICIAR_ARCHIVO_PARTIDAS', reiniciar_archivo_partidas)
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

    print("\n")
    for elemento in configuracion:
        print(f"{elemento}: {configuracion[elemento][0]} - {configuracion[elemento][1]}")
    print("\n")
    return configuracion
