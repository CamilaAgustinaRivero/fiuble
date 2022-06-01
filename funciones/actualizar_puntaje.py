# Ditrani, Elías Nicolás
"""
Función: actualizar_puntaje
Parámetros:
    intentos: cantidad de intentos en la ronda
    tabla: tabla con los puntajes anteriores de los usuarios
    usuario_ganador: nombre del usuario ganador
    usuario_perdedor: nombre del usuario perdedor
Salida:
    Devuelve la tabla de puntajes actualizada
"""

PUNTOS_NINGUN_ACIERTO_PRIMER_TURNO = -100
PUNTOS_NINGUN_ACIERTO_SEGUNDO_TURNO = -50


def actualizar_puntaje(puntos, tabla, usuario_actual, usuario_segundo):
    control = tabla.get(usuario_actual)
    if control is not None:
        tabla[usuario_actual] += puntos
    else:
        tabla[usuario_actual] = puntos

    if usuario_segundo != '':
        control = tabla.get(usuario_segundo)

        if control is not None:
            if puntos == PUNTOS_NINGUN_ACIERTO_PRIMER_TURNO:
                tabla[usuario_segundo] += PUNTOS_NINGUN_ACIERTO_SEGUNDO_TURNO
            else:
                tabla[usuario_segundo] += -puntos
        else:
            if puntos == PUNTOS_NINGUN_ACIERTO_PRIMER_TURNO:
                tabla[usuario_segundo] = PUNTOS_NINGUN_ACIERTO_SEGUNDO_TURNO
            else:
                tabla[usuario_segundo] = -puntos
    return tabla
