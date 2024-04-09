import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
import mysql.connector

listacampos = []
tablaactual = 0

def insertaBaseDatos():
    print("Insertamos en la base de datos")
    print(listacampos)
    peticion = "INSERT INTO "+tablaactual+" VALUES ("
    for campo in listacampos:
        peticion += "'"+campo.get()+"',"
    peticion = peticion[:-1]
    peticion += ")"
    print(peticion)

def seleccionaTabla(mitabla):
    global listacampos
    global tablaactual
    tablaactual = mitabla
    print("Has pulsado la tabla de: "+mitabla)
    for widget in contieneformulario.winfo_children():
        widget.destroy()
    cursor.execute("SHOW COLUMNS IN "+mitabla)
    columnas = cursor.fetchall()
    listacampos = []
    for columna in columnas:  
        ttk.Label(contieneformulario,text=columna[0]).pack(padx=5,pady=5)
        listacampos.append(ttk.Entry(contieneformulario))
        listacampos[-1].pack(padx=5,pady=5)
    ttk.Button(contieneformulario,text="Insertar",command=insertaBaseDatos).pack(padx=5,pady=5)
    
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
    ttk.Button(contienetablas,text=tabla[0],width=10,command=lambda tabla=tabla[0]:seleccionaTabla(tabla)).pack(padx=10,pady=10)

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
