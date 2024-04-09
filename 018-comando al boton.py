import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
import mysql.connector

def seleccionaTabla():
    print("Has pulsado un boton")
    
conexion = mysql.connector.connect(
    host="localhost",
    user="superc",
    password="superc",
    database="superc"
    )
cursor = conexion.cursor()

raiz = tk.Tk()
Style(theme='cosmo')

contienetablas = ttk.LabelFrame(
    raiz,
    text="Tablas en la BBDD",
    borderwidth=1,
    relief="ridge"
    )
contienetablas.grid(row=0,column=0,sticky="nsew",padx=5,pady=5)
cursor.execute("SHOW TABLES IN superc")
tablas = cursor.fetchall()
for tabla in tablas:
    ttk.Button(contienetablas,text=tabla[0],width=10,command=seleccionaTabla).pack(padx=10,pady=10)

contieneformulario = ttk.LabelFrame(
    raiz,
    text="Formulario de inserción",
    borderwidth=1,
    relief="ridge"
    )
contieneformulario.grid(row=0,column=1,sticky="nsew",padx=5,pady=5)
cursor.execute("SHOW COLUMNS IN productos")
columnas = cursor.fetchall()
for columna in columnas:  
    ttk.Label(contieneformulario,text=columna[0]).pack(padx=5,pady=5)
    ttk.Entry(contieneformulario).pack(padx=5,pady=5)


raiz.mainloop()
