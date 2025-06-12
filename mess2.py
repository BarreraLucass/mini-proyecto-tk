import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import time

# --- COLORES Y ESTILO ---
COLOR_FONDO = "#e4f4f5"
COLOR_RELOJ_BG = "#65ffea"
COLOR_RELOJ_FG = "#4B5BEC"
COLOR_BOTON_BG = "#3d8aee"
COLOR_BOTON_FG = "white"
COLOR_ENTRADA_BG = "#baf8f3"

# --- ventana principal ---
ventana = tk.Tk()
ventana.title("Mini Proyecto Tkinter")
ventana.geometry("500x500")
ventana.configure(bg=COLOR_FONDO)

pantallas = {}

def mostrar_pantalla(nombre):
    for pantalla in pantallas.values():
        pantalla.pack_forget()
    pantallas[nombre].pack(fill='both', expand=True)

# --- MENU ---
barra_menu = tk.Menu(ventana)
menu_pantallas = tk.Menu(barra_menu, tearoff=0)

menu_pantallas.add_command(label="Reloj", command=lambda: mostrar_pantalla("reloj"))
menu_pantallas.add_command(label="Tareas", command=lambda: mostrar_pantalla("tareas"))
menu_pantallas.add_command(label="Cronómetro", command=lambda: mostrar_pantalla("cronometro"))
menu_pantallas.add_command(label="Otras opciones", command=lambda: mostrar_pantalla("otras"))

barra_menu.add_cascade(label="Pantallas", menu=menu_pantallas)
ventana.config(menu=barra_menu)

# --- PANTALLA: RELOJ ---
frame_reloj = tk.Frame(ventana, bg=COLOR_FONDO)
reloj = tk.Label(frame_reloj, font=('Comic Sans MS', 40, 'bold'),
                 bg=COLOR_RELOJ_BG, fg=COLOR_RELOJ_FG, padx=20, pady=10)
reloj.pack(pady=80)

def actualizar_hora():
    reloj.config(text=time.strftime('%H:%M:%S'))
    ventana.after(1000, actualizar_hora)

actualizar_hora()
pantallas["reloj"] = frame_reloj

# --- PANTALLA: TAREAS ---
frame_tareas = tk.Frame(ventana, bg=COLOR_FONDO)
entrada_tarea = tk.Entry(frame_tareas, width=40, font=('Arial', 12), bg=COLOR_ENTRADA_BG)
entrada_tarea.pack(pady=10)

frame_lista = tk.Frame(frame_tareas, bg=COLOR_FONDO)
scrollbar = tk.Scrollbar(frame_lista)
lista_tareas = tk.Listbox(frame_lista, height=10, width=40,
                          yscrollcommand=scrollbar.set, font=('Arial', 11), bg=COLOR_ENTRADA_BG)
scrollbar.config(command=lista_tareas.yview)
lista_tareas.pack(side=tk.LEFT)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
frame_lista.pack(pady=10)

def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)

def eliminar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        lista_tareas.delete(seleccion)

tk.Button(frame_tareas, text="Agregar tarea", command=agregar_tarea,
          bg=COLOR_BOTON_BG, fg=COLOR_BOTON_FG, font=('Arial', 10, 'bold'), relief="flat").pack(pady=5)

tk.Button(frame_tareas, text="Eliminar tarea", command=eliminar_tarea,
          bg=COLOR_BOTON_BG, fg=COLOR_BOTON_FG, font=('Arial', 10, 'bold'), relief="flat").pack(pady=5)

pantallas["tareas"] = frame_tareas

# --- PANTALLA: CRONÓMETRO ---
frame_cronometro = tk.Frame(ventana, bg=COLOR_FONDO)
tiempo = 0
en_ejecucion = False

etiqueta_crono = tk.Label(frame_cronometro, text="00:00:00", font=('Arial', 36),
                          bg=COLOR_RELOJ_BG, fg=COLOR_RELOJ_FG, padx=20, pady=10)
etiqueta_crono.pack(pady=40)

def actualizar_cronometro():
    global tiempo
    if en_ejecucion:
        tiempo += 1
        h = tiempo // 3600
        m = (tiempo % 3600) // 60
        s = tiempo % 60
        etiqueta_crono.config(text=f"{h:02}:{m:02}:{s:02}")
        ventana.after(1000, actualizar_cronometro)

def iniciar():
    global en_ejecucion
    if not en_ejecucion:
        en_ejecucion = True
        actualizar_cronometro()

def pausar():
    global en_ejecucion
    en_ejecucion = False

def reiniciar():
    global tiempo, en_ejecucion
    en_ejecucion = False
    tiempo = 0
    etiqueta_crono.config(text="00:00:00")

tk.Button(frame_cronometro, text="Iniciar", command=iniciar,
          bg=COLOR_BOTON_BG, fg=COLOR_BOTON_FG, font=('Arial', 10, 'bold')).pack(pady=5)
tk.Button(frame_cronometro, text="Pausar", command=pausar,
          bg=COLOR_BOTON_BG, fg=COLOR_BOTON_FG, font=('Arial', 10, 'bold')).pack(pady=5)
tk.Button(frame_cronometro, text="Reiniciar", command=reiniciar,
          bg=COLOR_BOTON_BG, fg=COLOR_BOTON_FG, font=('Arial', 10, 'bold')).pack(pady=5)

pantallas["cronometro"] = frame_cronometro

# --- PANTALLA: OTRAS TAREAS ---
frame_otras = tk.Frame(ventana, bg=COLOR_FONDO)

# Calendario (selector de fecha básico con ComboBoxes)
tk.Label(frame_otras, text="Selecciona una fecha:",
         font=('Arial', 12), bg=COLOR_FONDO).pack(pady=5)

hoy = datetime.today()
dias = [str(i) for i in range(1, 32)]
meses = [str(i) for i in range(1, 13)]
años = [str(i) for i in range(hoy.year, hoy.year + 5)]

combo_dia = ttk.Combobox(frame_otras, values=dias, width=5)
combo_mes = ttk.Combobox(frame_otras, values=meses, width=5)
combo_año = ttk.Combobox(frame_otras, values=años, width=7)

combo_dia.set(str(hoy.day))
combo_mes.set(str(hoy.month))
combo_año.set(str(hoy.year))

combo_dia.pack(pady=2)
combo_mes.pack(pady=2)
combo_año.pack(pady=2)

# Notas
tk.Label(frame_otras, text="Notas rápidas:", font=('Arial', 12), bg=COLOR_FONDO).pack(pady=10)
nota_texto = tk.Text(frame_otras, height=8, width=40, bg=COLOR_ENTRADA_BG)
nota_texto.pack(pady=5)

pantallas["otras"] = frame_otras


# Función para actualizar la hora y verificar la alarma
def actualizar_hora():
    ahora = time.strftime("%H:%M:%S")
    etiqueta_hora.config(text=ahora)
    
    if alarma_hora.get() == ahora:
        messagebox.showinfo("Alarma", "¡Es hora de la alarma!")
        # Puedes agregar un sonido aquí si quieres
        alarma_hora.set("")  # Resetear alarma después de sonar
    root.after(1000, actualizar_hora)

# Función para establecer la alarma
def establecer_alarma():
    hora_alarma = entrada_hora.get()
    alarma_hora.set(hora_alarma)

# Crear la ventana principal
root = tk.Toplevel(ventana)
root.title("Reloj con Alarma")
root.geometry("300x150")

# Variable para la hora de la alarma
alarma_hora = tk.StringVar()

# Mostrar la hora actual
etiqueta_hora = tk.Label(root, font=("Helvetica", 24))
etiqueta_hora.pack(pady=10)

# Entrada para la hora de la alarma
tk.Label(root, text="Ingrese hora de alarma (HH:MM:SS):").pack()
entrada_hora = tk.Entry(root)
entrada_hora.pack()

# Botón para establecer alarma
boton_establecer = tk.Button(root, text="Establecer alarma", command=establecer_alarma)
boton_establecer.pack(pady=5)

# Iniciar actualización del reloj
actualizar_hora()

# Ejecutar la interfaz
root.mainloop()
# --- pantalla inicial ---
mostrar_pantalla("reloj")


ventana.mainloop()