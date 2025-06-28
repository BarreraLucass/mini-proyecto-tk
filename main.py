import tkinter as tk
from reloj import Reloj
from alarma import Alarma
from tareas import PantallaTareas
from cronometro import PantallaCronometro
from bienvenida import PantallaBienvenida  

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mini Proyecto Tkinter")
        self.geometry("500x500")
        self.configure(bg="#e4f4f5")

        
        icono = tk.PhotoImage(file='alarm.png')
        self.iconphoto(True, icono)

        
        self.pantalla_bienvenida = PantallaBienvenida(self, self.iniciar_aplicacion)
        self.pantalla_bienvenida.pack(fill="both", expand=True)

    def iniciar_aplicacion(self):
        """Se ejecuta cuando el usuario hace clic en 'Ingresar a la aplicación'."""
        self.pantalla_bienvenida.pack_forget()

       
        self.pantallas = {
            "reloj": Reloj(self),
            "alarma": Alarma(self),
            "tareas": PantallaTareas(self),
            "cronometro": PantallaCronometro(self)
        }

        barra_menu = tk.Menu(self)
        menu_pantallas = tk.Menu(barra_menu, tearoff=0)

        for nombre in self.pantallas:
            menu_pantallas.add_command(label=nombre.capitalize(), command=lambda n=nombre: self.mostrar_pantalla(n))

        barra_menu.add_cascade(label="Pantallas", menu=menu_pantallas)
        self.config(menu=barra_menu)

        self.mostrar_pantalla("reloj")  

    def mostrar_pantalla(self, nombre):
        """Muestra la pantalla seleccionada desde el menú."""
        for pantalla in self.pantallas.values():
            pantalla.pack_forget()
        self.pantallas[nombre].pack(fill="both", expand=True)

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
