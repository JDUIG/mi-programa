import tkinter as tk
from tkinter import messagebox

def calcular_pendiente():
    try:
        pedida = float(entry_pedida.get())
        pagada = float(entry_pagada.get())
        pendiente = pedida - pagada

        entry_pendiente.delete(0, tk.END)
        entry_pendiente.insert(0, f"{pendiente:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Introduce números válidos")

ventana = tk.Tk()
ventana.title("Cálculo de dinero pendiente")
ventana.geometry("320x220")

tk.Label(ventana, text="Cantidad pedida").pack()
entry_pedida = tk.Entry(ventana)
entry_pedida.pack()

tk.Label(ventana, text="Cantidad pagada").pack()
entry_pagada = tk.Entry(ventana)
entry_pagada.pack()

tk.Label(ventana, text="Cantidad pendiente").pack()
entry_pendiente = tk.Entry(ventana)
entry_pendiente.pack()

tk.Button(ventana, text="Calcular", command=calcular_pendiente).pack(pady=10)

ventana.mainloop()
