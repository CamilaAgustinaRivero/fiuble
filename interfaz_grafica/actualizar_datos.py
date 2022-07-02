from cargar_datos import cargar_datos_usuarios
from validar import validar_clave, validar_usuario
from tkinter import messagebox

def actualizar_datos_usuarios(usuario, clave, clave_reingreso):
    dict_datos = cargar_datos_usuarios()
    ar_datos_usuarios = open("interfaz_grafica\datos_usuarios.csv", "a") 
    usuario_valido = validar_usuario(usuario)
    claves_iguales = clave == clave_reingreso
    clave_valida = validar_clave(clave)
    if usuario in dict_datos.keys():
        messagebox.showinfo(title=None, message="El usuario ingresado ya existe!")
    else:
        if usuario_valido and clave_valida and claves_iguales:
            ar_datos_usuarios.write(f"{usuario},{clave}")
            messagebox.showinfo(title=None, message="Usuario Registrado!")
        else:
            if not usuario_valido:
                messagebox.showerror(title=None, message="Nombre de usuario incorrecto")
            elif usuario_valido and not claves_iguales:
                messagebox.showerror(title=None, message="Las claves no coinciden")
            elif usuario_valido and not clave_valida:
                messagebox.showerror(title=None, message="La clave ingresada no es valida")
            else:
                messagebox.showerror(title=None, message="Alguno de los datos ingresados es incorrecto") 
    ar_datos_usuarios.close()