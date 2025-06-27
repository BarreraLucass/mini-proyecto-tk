import tkinter as tk
import time
from tkinter import messagebox
import winsound
import re
import json
import os

class Alarma(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#e4f4f5")

        self.etiqueta_hora = tk.Label(self, font=("Helvetica", 24))
        self.etiqueta_hora.pack(pady=10)

        self.entrada_nombre = tk.Entry(self, font=('Arial', 12))
        self.entrada_nombre.pack()

        tk.Label(self, text="Ingrese hora de alarma (HH:MM):", font=('Arial', 12)).pack()
        self.entrada_hora = tk.Entry(self)
        self.entrada_hora.pack()

        tk.Label(self, text="Alarmas activas:", font=("Arial", 12)).pack(pady=(10, 0))
        self.lista_alarmas = tk.Listbox(self, height=10, width=40, font=("Arial", 11))
        self.lista_alarmas.pack(pady=5)

        self.boton_establecer = tk.Button(self, text="Establecer alarma", command=self.agregar_alarma)
        self.boton_establecer.pack(pady=5)

        self.boton_eliminar = tk.Button(self, text="Eliminar alarma seleccionada", command=self.eliminar_alarma)
        self.boton_eliminar.pack(pady=5)
    
        self.alarmas = []

        self.actualizar_hora() 
        
        self.cargar_alarmas()
    
    def validar_hora(self, hora):
        patron = re.compile(r"^(2[0-3]|[01]?\d):[0-5]?\d:[0-5]?\d$")
        return patron.match(hora)

    def actualizar_hora(self):
        ahora = time.strftime("%H:%M:%S")
        self.etiqueta_hora.config(text=ahora)

        for alarma in self.alarmas:
            if alarma['hora'] == ahora:
                try:
                    winsound.Beep(1000, 1000)
                except RuntimeError:
                    print("No se pudo reproducir el beep. Mostrando sólo el mensaje.")
                    messagebox.showinfo("Alarma", "¡Es hora de la alarma!")

        self.after(1000, self.actualizar_hora)

    def agregar_alarma(self):
        hora = self.entrada_hora.get().strip()
        nombre = self.entrada_nombre.get().strip()
        if self.validar_hora(hora):
            if not any(alarma['hora'] == hora and alarma['nombre'] == nombre for alarma in self.alarmas):
                nueva_alarma = {"hora": hora, "nombre": nombre}
                self.alarmas.append(nueva_alarma)
                self.lista_alarmas.insert(tk.END, f"{hora} - {nombre if nombre else 'Sin nombre'}")
                self.guardar_alarmas()
                self.entrada_hora.delete(0, tk.END)
                self.entrada_nombre.delete(0, tk.END)
            else:
                messagebox.showinfo("Duplicada", "Esta alarma ya está activa, capo")
        else:
            messagebox.showerror("Formato inválido", "Usá el formato HH:MM:SS (ej: 07:30:00)")
    
    def eliminar_alarma(self):
        seleccion = self.lista_alarmas.curselection()
        if not seleccion:
            messagebox.showinfo("Sin selección", "Seleccioná una alarma para eliminar.")
            return
        indice = seleccion[0]
        self.lista_alarmas.delete(indice)
        del self.alarmas[indice]
        self.guardar_alarmas()

    def guardar_alarmas(self):
        with open("alarmas.json", "w") as archivo:
           json.dump(self.alarmas, archivo)

    def cargar_alarmas(self):
        if os.path.exists("alarmas.json"):
             with open("alarmas.json", "r") as archivo:
                try:
                    self.alarmas = json.load(archivo)
                    for alarma in self.alarmas:
                        hora = alarma["hora"]
                        nombre = alarma["nombre"]
                        self.lista_alarmas.insert(tk.END, f"{hora} - {nombre if nombre else 'Sin nombre'}")
                except json.JSONDecodeError:
                    self.alarmas = []
      

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Alarma")
    app = Alarma(master=root)
    app.pack(padx=20, pady=20)
    root.mainloop()
