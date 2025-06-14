import tkinter as tk
from pantallas import PantallaBase

class PantallaTareas(PantallaBase):
    def __init__(self, master):
        super().__init__(master)
        self.entrada_tarea = tk.Entry(self, width=40)
        self.entrada_tarea.pack(pady=10)

        self.lista_tareas = tk.Listbox(self, height=10, width=40)
        self.lista_tareas.pack(pady=10)

        tk.Button(self, text="Agregar tarea", command=self.agregar_tarea).pack()
        tk.Button(self, text="Eliminar tarea", command=self.eliminar_tarea).pack()

    def agregar_tarea(self):
        tarea = self.entrada_tarea.get()
        if tarea:
            self.lista_tareas.insert(tk.END, tarea)
            self.entrada_tarea.delete(0, tk.END)

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            self.lista_tareas.delete(seleccion)