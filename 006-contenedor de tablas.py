import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

raiz = tk.Tk()
Style(theme='cosmo')

contienetablas = ttk.LabelFrame(
    raiz,
    text="Tablas en la BBDD",
    borderwidth=1,
    relief="ridge"
    )
contienetablas.pack(padx=5,pady=5)
ttk.Button(contienetablas,text="Clientes").pack(padx=50,pady=10)
ttk.Button(contienetablas,text="Productos").pack(padx=50,pady=10)

raiz.mainloop()
