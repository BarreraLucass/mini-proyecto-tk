import tkinter as tk
from estilos import COLOR_FONDO, COLOR_BOTON_BG, COLOR_BOTON_FG

class PantallaBienvenida(tk.Frame):
    def __init__(self, master, continuar_callback):
        super().__init__(master, bg=COLOR_FONDO)

        tk.Label(
            self,
            text="Bienvenido a nuestro Mini Proyecto Tkinter",
            font=("Arial", 18, "bold"),
            bg=COLOR_FONDO
        ).pack(pady=15)

        tk.Label(
            self,
            text="Grupo 3",
            font=("Arial", 16),
            bg=COLOR_FONDO,
            fg="#333"
        ).pack(pady=5)

        integrantes = [
            "Manuel Lautaro Visñuk",
            "María Alejandra Roldán Barrera",
            "Lucas Sebastián",
            "Matias Geymonat",
            "Santiago Cabaña",
            "Joana Margarita Perez",
            "Lucas Beneventano"
        ]

        for nombre in integrantes:
            tk.Label(self, text=nombre, font=("Arial", 12), bg=COLOR_FONDO).pack()

        tk.Button(
            self,
            text="Ingresar a la aplicación",
            bg=COLOR_BOTON_BG,
            fg=COLOR_BOTON_FG,
            command=continuar_callback
        ).pack(pady=20)
