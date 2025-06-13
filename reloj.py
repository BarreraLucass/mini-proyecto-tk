import tkinter as tk
import time



class Reloj(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#e4f4f5")
        self.reloj = tk.Label(self, font=('Arial', 40, 'bold'), bg="#65ffea", fg="#4B5BEC")
        self.reloj.pack(pady=80)
        self.actualizar_hora()
        self.pack()
    

    def actualizar_hora(self):
        self.reloj.config(text=time.strftime('%H:%M:%S'))
        self.after(1000, self.actualizar_hora)


root = tk.Tk()
root.title("Reloj")
reloj = Reloj(root)
root.mainloop()
