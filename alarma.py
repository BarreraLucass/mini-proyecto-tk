import tkinter as tk
import time
from tkinter import messagebox
import winsound

class Alarma(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#e4f4f5")

        self.alarma_hora = tk.StringVar()

        self.etiqueta_hora = tk.Label(self, font=("Helvetica", 24))
        self.etiqueta_hora.pack(pady=10)

        tk.Label(self, text="Ingrese hora de alarma (HH:MM):", font=('Arial', 12)).pack()
        self.entrada_hora = tk.Entry(self)
        self.entrada_hora.pack()

        self.boton_establecer = tk.Button(self, text="Establecer alarma", command=self.establecer_alarma)
        self.boton_establecer.pack(pady=5)

        self.actualizar_hora() 

    def actualizar_hora(self):
        ahora = time.strftime("%H:%M")
        self.etiqueta_hora.config(text=ahora)

        if self.alarma_hora.get() == ahora:
            winsound.Beep(1000, 1000)
            messagebox.showinfo("Alarma", "¡Es hora de la alarma!")
            self.alarma_hora.set("")

        self.after(1000, self.actualizar_hora)

    def establecer_alarma(self):
        self.alarma_hora.set(self.entrada_hora.get())

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Alarma")
    app = Alarma(master=root)
    app.pack(padx=20, pady=20)
    root.mainloop()
