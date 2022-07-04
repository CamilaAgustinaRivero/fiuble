from tkinter import *
from tkinter import messagebox


def obtener_usuarios_claves():
    usuarios_claves={
        "German": "key123",
        "Camila": "pro571",
        "Daniel": "reg708",
        "Federico": "les446",
        "Elias": "wot798",
    }
    return usuarios_claves

def validar_clave(nombre_usuario, clave_usuario):
        claves = obtener_usuarios_claves()
        if nombre_usuario in claves.keys():
            if claves[nombre_usuario] == clave_usuario:
                messagebox.showinfo(title=None, message="Usuario y Clave Correctos")
            else:
                messagebox.showerror(title=None, message="Algunos de los datos ingresados es Incorrecto")
        else:
            messagebox.showerror(title=None, message="Algunos de los datos ingresados es Incorrecto")


def ventana_login():
    raiz = Tk()
    raiz.title("Login Sortija")
    raiz.resizable(True, True)
    raiz.iconbitmap('sortija.ico')
    raiz.config(bg="black")
    
    marco = Frame(raiz)
    marco.config(width=300, height=130, bg="black")
    marco.pack()

    #Casilla de Usuario
    mensaje_user = Label(marco, text="Usuario: ")
    mensaje_user.grid(row=0, column=0, sticky= "e", padx=10, pady=10)

    entry_user = Entry(marco)
    entry_user.grid(row=0, column=1, padx=10, pady=10)
    
    #Casilla de clave
    mensaje_pw = Label(marco, text="Clave: ")
    mensaje_pw.grid(row=1, column=0, sticky= "e", padx=10, pady=10)

    entry_pw = Entry(marco, show="*")
    entry_pw.grid(row=1, column=1, padx=10, pady=10)
    
    #Boton enviar formulario
    
    botonEnvio=Button(marco, text="Ingresar", command=lambda:validar_clave(entry_user.get(),entry_pw.get()))
    botonEnvio.grid(row=2, column=0, padx=10, pady=10)
    botonEnvio=Button(marco, text="Registrarse")
    botonEnvio.grid(row=2, column=1, padx=10, pady=10)
    
    raiz.mainloop()
         
ventana_login()
