import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

raiz = tk.Tk()

ttk.Button(raiz,text="Clientes").pack(padx=50,pady=10)
ttk.Button(raiz,text="Productos").pack(padx=50,pady=10)

raiz.mainloop()
