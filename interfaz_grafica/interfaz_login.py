from tkinter import *
from validaciones_interfaz import verificar_ingreso_clave
from form_registro import form_registro

# Daniel, Gonzalez
"""
Función: casilla_usuario_y_clave()
Parámetros:
    numero_usuario: variable que guarda el numero de usuario a enseñar por la interfaz
    fila: refiere a la posición en la que se quiere colocar la casilla del usuario
    marco: marco empaquetado de la interfaz
Salidas:
"""

def casilla_usuario_y_clave(numero_usuario, fila, marco):
    # Casilla usuario
    mensaje_user = Label(marco, text=f"Usuario {numero_usuario}: ")
    mensaje_user.grid(row=fila, column=0, sticky="e", padx=10, pady=10)
    entry_user = Entry(marco)
    entry_user.grid(row=fila, column=1, padx=10, pady=10)

    # Casilla de clave
    entry_pw = Entry(marco, show="*")
    mensaje_pw = Label(marco, text="Clave: ")
    mensaje_pw.grid(row=fila + 1, column=0, sticky="e", padx=10, pady=10)
    entry_pw.grid(row=fila + 1, column=1, padx=10, pady=10)
    return entry_user, entry_pw

# Daniel, Gonzalez
"""
Función: ventana_login()
Parámetros:
    modo_de_juego: opción escogida a jugar '1' para 1 jugador o '2' para 2 jugadores
    raiz_main: raiz de la interfaz que permite manipularla luego de su uso
Salidas:
"""

def ventana_login(modo_de_juego, raiz_main):
    raiz = Tk()
    raiz.title("Login Sortija")
    raiz.resizable(False, False)
    raiz.iconbitmap('logo_wordle.ico')
    raiz.config(bg="blue")

    marco = Frame(raiz)
    marco.config(width=300, height=130, bg="green")
    marco.pack()

    if modo_de_juego == 2:
        entry_user1, entry_pw1 = casilla_usuario_y_clave(1, 0, marco)
        entry_user2, entry_pw2 = casilla_usuario_y_clave(2, 2, marco)
        botonEnvio = Button(marco, text="Entrar",
                            command=lambda: verificar_ingreso_clave(entry_user1.get(), entry_pw1.get(), modo_de_juego,
                                                                    raiz, raiz_main, entry_user2.get(), entry_pw2.get()))
    else:
        entry_user1, entry_pw1 = casilla_usuario_y_clave(1, 0, marco)
        botonEnvio = Button(marco, text="Entrar",
                            command=lambda: verificar_ingreso_clave(entry_user1.get(), entry_pw1.get(), modo_de_juego,
                                                                    raiz, raiz_main))

    # Boton enviar formulario
    botonEnvio.grid(row=5, column=1, padx=10, pady=10)

    botonRegistro = Button(marco, text="Registrarse", command=lambda: form_registro())
    botonRegistro.grid(row=6, column=1, padx=10, pady=10)

    raiz.mainloop()
