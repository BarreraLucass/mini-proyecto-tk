import tkinter as tk
import time
from tkinter import messagebox
import winsound
from estilos import COLOR_ENTRADA_BG, COLOR_BOTON_BG, COLOR_BOTON_FG

class Alarma(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#e4f4f5")

        self.alarma_hora = tk.StringVar()

        self.etiqueta_hora = tk.Label(self, font=("Helvetica", 24), bg="#e4f4f5")
        self.etiqueta_hora.pack(pady=10)

        tk.Label(self, text="Ingrese hora de alarma (HH:MM):", font=('Arial', 12), bg="#e4f4f5").pack()
        self.entrada_hora = tk.Entry(self, bg=COLOR_ENTRADA_BG)
        self.entrada_hora.pack()

        self.boton_establecer = tk.Button(
            self,
            text="Establecer alarma",
            bg=COLOR_BOTON_BG,
            fg=COLOR_BOTON_FG,
            command=self.establecer_alarma
        )
        self.boton_establecer.pack(pady=5)

        self.actualizar_hora() 

    def actualizar_hora(self):
        ahora = time.strftime("%H:%M")
        self.etiqueta_hora.config(text=ahora)

        if self.alarma_hora.get() == ahora:
            winsound.Beep(1000, 1000)
            messagebox.showinfo("Alarma", "¡Es hora de la alarma!")
            self.alarma_hora.set("")  # Resetea la alarma

        self.after(1000, self.actualizar_hora)

    def establecer_alarma(self):
        entrada = self.entrada_hora.get()
        if ":" in entrada and len(entrada) == 5:
            self.alarma_hora.set(entrada)
        else:
            messagebox.showwarning("Formato inválido", "Usá formato HH:MM")
