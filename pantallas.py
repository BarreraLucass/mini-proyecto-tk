import tkinter as tk

class PantallaBase(tk.Frame):
    """Clase base para todas las pantallas."""
    def __init__(self, master):
        super().__init__(master, bg="#e4f4f5")

    def mostrar(self):
        """Muestra esta pantalla y oculta las demás."""
        for widget in self.master.winfo_children():
            widget.pack_forget()
        self.pack(fill="both", expand=True)