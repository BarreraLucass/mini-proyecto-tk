import tkinter as tk
import time
from estilos import COLOR_RELOJ_BG, COLOR_RELOJ_FG

class Reloj(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#e4f4f5")
        self.reloj = tk.Label(
            self,
            font=('Comic Sans MS', 40, 'bold'),
            bg=COLOR_RELOJ_BG,
            fg=COLOR_RELOJ_FG
        )
        self.reloj.pack(pady=80)
        self.actualizar_hora()

    def actualizar_hora(self):
        self.reloj.config(text=time.strftime('%H:%M:%S'))
        self.after(1000, self.actualizar_hora)

