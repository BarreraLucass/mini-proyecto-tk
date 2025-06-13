import tkinter as tk
import time
from tkinter import messagebox

class Alarma(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#e4f4f5")

        # Variable para la hora de la alarma
        self.alarma_hora = tk.StringVar()

        # Label para mostrar la hora actual
        self.etiqueta_hora = tk.Label(self, font=("Helvetica", 24))
        self.etiqueta_hora.pack(pady=10)

        # Entrada para la hora de la alarma
        tk.Label(self, text="Ingrese hora de alarma (HH:MM:SS):", font=('Arial', 12)).pack()
        self.entrada_hora = tk.Entry(self)
        self.entrada_hora.pack()

        # Botón para establecer la alarma
        self.boton_establecer = tk.Button(self, text="Establecer alarma", command=self.establecer_alarma)
        self.boton_establecer.pack(pady=5)

        # Iniciar actualización del reloj
        self.actualizar_hora()

    def actualizar_hora(self):
        """Actualiza la hora y verifica si debe sonar la alarma."""
        ahora = time.strftime("%H:%M:%S")
        self.etiqueta_hora.config(text=ahora)

        if self.alarma_hora.get() == ahora:
            messagebox.showinfo("Alarma", "¡Es hora de la alarma!")
            self.alarma_hora.set("")  # Resetear alarma después de sonar

        self.after(1000, self.actualizar_hora)

    def establecer_alarma(self):
        """Guarda la hora de la alarma ingresada por el usuario."""
        self.alarma_hora.set(self.entrada_hora.get())






#####    Estoy probando algo x eso dejo el codigo aca por las dudas jeje



""""

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


######
Version de Joa

frame_alarma = tk.Frame(ventana, bg=COLOR_FONDO)

def actualizar_hora():
    ahora = time.strftime("%H:%M:%S")
    etiqueta_hora.config(text=ahora)
    
    if alarma_hora.get() == ahora:
        messagebox.showinfo("Alarma", "¡Es hora de la alarma!")
        # Puedes agregar un sonido aquí si quieres
        alarma_hora.set()  # Resetear alarma después de sonar
    frame_alarma.after(1000, actualizar_hora)

# Función para establecer la alarma
def establecer_alarma():
    hora_alarma = entrada_hora.get()
    alarma_hora.set(hora_alarma)



# Variable para la hora de la alarma
alarma_hora = tk.StringVar()

# Mostrar la hora actual
etiqueta_hora = tk.Label(frame_alarma, font=("Helvetica", 24))
etiqueta_hora.pack(pady=10)

# Entrada para la hora de la alarma
tk.Label(frame_alarma, text="Ingrese hora de alarma :(HH:MM:SS) ").pack()
entrada_hora = tk.Entry(frame_alarma)
entrada_hora.pack()

# Botón para establecer alarma
boton_establecer = tk.Button(frame_alarma, text="Establecer alarma", command=establecer_alarma)
boton_establecer.pack(pady=5)

# Sonido de alarma


# Iniciar actualización del reloj
actualizar_hora()

pantallas["alarma"] = frame_alarma





"""