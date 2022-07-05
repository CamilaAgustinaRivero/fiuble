from tkinter import *
from actualizar_datos import actualizar_datos_usuarios


def form_registro():
    raiz = Tk()
    raiz.title("Registro")
    raiz.resizable(False, False)
    raiz.iconbitmap('logo_wordle.ico')
    raiz.config(bg="blue")

    marco = Frame(raiz)
    marco.config(width=300, height=130, bg="green")
    marco.pack()

    # Casilla de Usuario
    mensaje_user = Label(marco, text="Usuario: ")
    mensaje_user.grid(row=0, column=0, sticky="e", padx=10, pady=10)

    entry_user = Entry(marco)
    entry_user.grid(row=0, column=1, padx=10, pady=10)

    # Casilla de clave
    mensaje_pw = Label(marco, text="Clave: ")
    mensaje_pw.grid(row=1, column=0, sticky="e", padx=10, pady=10)

    entry_pw = Entry(marco, show="*")
    entry_pw.grid(row=1, column=1, padx=10, pady=10)

    # Casilla de reingreso de clave
    mensaje_reingreso = Label(marco, text="Reingrese Clave: ")
    mensaje_reingreso.grid(row=2, column=0, sticky="e", padx=10, pady=10)

    entry_reingreso = Entry(marco, show="*")
    entry_reingreso.grid(row=2, column=1, padx=10, pady=10)

    # Boton enviar formulario

    botonEnvio = Button(marco, text="Enviar Formulario",
                        command=lambda: actualizar_datos_usuarios(entry_user.get(), entry_pw.get(),
                                                                  entry_reingreso.get(), raiz))
    botonEnvio.grid(row=3, column=1, padx=10, pady=10)

    raiz.mainloop()
