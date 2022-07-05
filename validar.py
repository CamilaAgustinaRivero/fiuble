from tkinter import messagebox
from cargar_datos import cargar_datos_usuarios

def validar_clave(clave):
    letras_con_acentos = ["á","é","í","ó","ú"]
    tiene_acento = tiene_mayus = tiene_minus = tiene_num = caracter_especial = caracter_dif = False
    for caracter in clave:
        if caracter in letras_con_acentos:
            tiene_acento = True
        elif caracter.islower():
            tiene_minus = True
        elif caracter.isupper():
            tiene_mayus = True
        elif caracter.isdigit():
            tiene_num = True
        elif caracter in ["_", "-"]:
            caracter_especial = True
        elif not caracter.isalpha or not caracter.isdigit():
            caracter_dif = True
    clave_valida = 8 <= len(clave) <= 15 and tiene_num and tiene_mayus and tiene_minus and not tiene_acento and caracter_especial and not caracter_dif
    return clave_valida

def validar_usuario(usuario):
    caracteres_alpha = [caracter.isalpha() for caracter in usuario]
    caracteres_num = [caracter.isdigit() for caracter in usuario]
    caracter_invalido = False
    for caracter in usuario:
        if caracter.isalpha() or caracter.isdigit() or caracter == "_":
            continue
        else:
            print(caracter, "invalido")
            caracter_invalido = True
    usuario_valido =  4 <= len(usuario) <= 15 and any(caracteres_alpha) and any(caracteres_num) and ("_" in usuario) and not caracter_invalido
    return usuario_valido

def verificar_ingreso_clave(nombre_usuario, clave_usuario):
    claves = cargar_datos_usuarios()
    if nombre_usuario in claves.keys():
        if claves[nombre_usuario] == clave_usuario:
            messagebox.showinfo(title=None, message="Usuario y Clave Correctos (Empezar juego?)")
        else:
            messagebox.showerror(title=None, message="Alguno de los datos ingresados es Incorrecto")
    else:
        messagebox.showerror(title=None, message="Algunos de los datos ingresados es Incorrecto")
