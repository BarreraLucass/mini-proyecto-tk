import tkinter as tk
import time
from tkinter import messagebox

class Alarma(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#e4f4f5")
        tk.Label(self, text="Ingrese hora de alarma:", font=('Arial', 12)).pack()
        self.entrada_hora = tk.Entry(self)
        self.entrada_hora.pack()
        self.boton_establecer = tk.Button(self, text="Establecer alarma", command=self.establecer_alarma)
        self.boton_establecer.pack(pady=5)
        self.alarma_hora = ""

    def establecer_alarma(self):
        self.alarma_hora = self.entrada_hora.get()
