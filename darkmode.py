"""
    el parametro widget es la ventana principal donde se va a aplicar el cambio de modo y el parametro modo_actual es la cadena que va a indicar el modo actual
    y va a retornar un string con el nuevo modo oscuro si estaba en claro o claro si estaba en oscuro
    """
def aplicar_darkmode(widget, modo_actual):

    #colores segun el modo actual
    nuevo_bg = "#000000" if modo_actual == "claro" else "#e4f4f5"
    nuevo_fg = "white" if modo_actual == "claro" else "black"


    def aplicar_a_todos(widg):
        opciones = widg.keys()
        if 'bg' in opciones:
            widg.configure(bg=nuevo_bg)
        if 'fg' in opciones:
            widg.configure(fg=nuevo_fg)

        for hijo in widg.winfo_children():
            aplicar_a_todos(hijo)

    aplicar_a_todos(widget)

    return "oscuro" if modo_actual == "claro" else "claro"


