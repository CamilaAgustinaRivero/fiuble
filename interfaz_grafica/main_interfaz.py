from tkinter import *
from interfaz_login import ventana_login


def main_interfaz():
    raiz = Tk()
    raiz.title("Fiuble")
    raiz.resizable(False, False)
    raiz.iconbitmap('logo_wordle.ico')
    raiz.config(bg="blue")

    marco = Frame(raiz)
    marco.config(width=300, height=130, bg="green")
    marco.pack()

    # Botones de opcion de modo de juego
    modo_de_juego = IntVar()
    opcion_1 = Radiobutton(marco, text="1 jugador", padx=20, variable=modo_de_juego, value=1, bg="green")
    opcion_1.grid(row=0, column=0)
    opcion_2 = Radiobutton(marco, text="2 jugadores", padx=20, variable=modo_de_juego, value=2, bg="green")
    opcion_2.grid(row=1, column=0)

    boton_continuar = Button(marco, text="Jugar Fiuble", command=lambda: ventana_login(modo_de_juego.get()))
    boton_continuar.grid(row=2, column=0, padx=10, pady=10)

    raiz.mainloop()


main_interfaz()
