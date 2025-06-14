import tkinter as tk
from pantallas import PantallaBase

class PantallaCronometro(PantallaBase):
    def __init__(self, master):
        super().__init__(master)
        self.tiempo = 0
        self.en_ejecucion = False
        self.etiqueta_crono = tk.Label(self, text="00:00:00", font=('Arial', 36), bg="#65ffea")
        self.etiqueta_crono.pack(pady=40)

        tk.Button(self, text="Iniciar", command=self.iniciar).pack()
        tk.Button(self, text="Pausar", command=self.pausar).pack()
        tk.Button(self, text="Reiniciar", command=self.reiniciar).pack()

    def actualizar_cronometro(self):
        if self.en_ejecucion:
            self.tiempo += 1
            h, m, s = self.tiempo // 3600, (self.tiempo % 3600) // 60, self.tiempo % 60
            self.etiqueta_crono.config(text=f"{h:02}:{m:02}:{s:02}")
            self.after(1000, self.actualizar_cronometro)

    def iniciar(self):
        if not self.en_ejecucion:
            self.en_ejecucion = True
            self.actualizar_cronometro()

    def pausar(self):
        self.en_ejecucion = False

    def reiniciar(self):
        self.en_ejecucion = False
        self.tiempo = 0
        self.etiqueta_crono.config(text="00:00:00")