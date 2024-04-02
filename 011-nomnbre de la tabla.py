import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
import mysql.connector

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
contienetablas.pack(padx=5,pady=5)
cursor.execute("SHOW TABLES IN superc")
tablas = cursor.fetchall()
for tabla in tablas:
    nombre_de_la_tabla = tabla[0]
    ttk.Button(contienetablas,text=nombre_de_la_tabla,width=10).pack(padx=10,pady=10)

raiz.mainloop()
