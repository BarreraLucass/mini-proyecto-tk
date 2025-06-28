import tkinter as tk
from reloj import Reloj
from alarma import Alarma
from tareas import PantallaTareas
from cronometro import PantallaCronometro
from darkmode import aplicar_darkmode


class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mini Proyecto Tkinter")
        self.geometry("500x500")
        self.configure(bg="#e4f4f5")

        # Icono
        icono = tk.PhotoImage(file='alarm.png')
        self.iconphoto(True, icono)


        
        # BOTÓN MODO OSCURO/CLARO
        self.modo = "claro"
        self.boton_modo = tk.Button(self, text="Modo Oscuro", command=self.toggle_modo)
        self.boton_modo.pack(side="top", pady=5)

        # Crear pantallas
        self.pantallas = {
            "reloj": Reloj(self),
            "alarma": Alarma(self),
            "tareas": PantallaTareas(self),
            "cronometro": PantallaCronometro(self)
        }

        # Agregar menú para cambiar entre pantallas
        barra_menu = tk.Menu(self)
        menu_pantallas = tk.Menu(barra_menu, tearoff=0)

        for nombre in self.pantallas:
            menu_pantallas.add_command(label=nombre.capitalize(), command=lambda n=nombre: self.mostrar_pantalla(n))

        barra_menu.add_cascade(label="Pantallas", menu=menu_pantallas)
        self.config(menu=barra_menu)

        self.mostrar_pantalla("reloj")


        
    def toggle_modo(self):
        self.modo = aplicar_darkmode(self, self.modo)
        self.boton_modo.configure(text="Modo Claro" if self.modo == "oscuro" else "Modo Oscuro")

    def mostrar_pantalla(self, nombre):
        """Cambia la pantalla visible."""
        for pantalla in self.pantallas.values():
            pantalla.pack_forget()
        self.pantallas[nombre].pack(fill="both", expand=True)

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()