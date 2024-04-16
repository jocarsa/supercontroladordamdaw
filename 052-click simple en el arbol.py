import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
import mysql.connector

listacampos = []
tablaactual = 0
identificador_seleccionado = 0

def eliminaRegistro():
    print("Voy a eliminar el registro que está seleccionado")
    print("La tabla seleccionada es: "+tablaactual)
    print("El identificador seleccionado es: "+str(identificador_seleccionado))
    peticion = f"DELETE FROM {tablaactual} WHERE Identificador = {identificador_seleccionado};"
    print(peticion)
    cursor.execute(peticion)
    conexion.commit()
    seleccionaTabla(tablaactual)
    
def clickEnArbol(event):
    global identificador_seleccionado
    print("Has hecho click en el arbol")
    elemento = arbol.identify('item',event.x,event.y)
    arbol.selection_set(elemento)
    print(elemento)
    valores = arbol.item(elemento,'values')
    print(valores)
    identificador_seleccionado = valores[0]

def insertaBaseDatos():
    print("Insertamos en la base de datos")
    print(listacampos)
    peticion = "INSERT INTO "+tablaactual+" VALUES (NULL,"
    
    for campo in range(0,len(listacampos)):
        if campo != 0:
            peticion += "'"+listacampos[campo].get()+"',"
    peticion = peticion[:-1]
    peticion += ")"
    print(peticion)
    cursor.execute(peticion)
    conexion.commit()
    seleccionaTabla(tablaactual)

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
    # Vacío el arbol
    for elemento in arbol.get_children():
        arbol.delete(elemento)
    for columna in arbol['columns']:
        arbol.column(columna,width=0)
        arbol.heading(columna,text='')
    # ahora relleno el arbol con los datos que tocan
    cursor.execute("SHOW COLUMNS IN "+mitabla)
    columnas = cursor.fetchall()
    listadocolumnas = []
    for columna in columnas:
        listadocolumnas.append(columna[0])
    listadocolumnas = tuple(listadocolumnas)
    print(listadocolumnas)
    arbol['columns'] = listadocolumnas
    for unacolumna in listadocolumnas:
        arbol.heading(unacolumna,text=unacolumna)
        arbol.column(unacolumna,width=100)
    cursor.execute("SELECT * FROM "+mitabla)
    registros = cursor.fetchall()
    for registro in registros:
        arbol.insert('','end',values=registro)
    
conexion = mysql.connector.connect(
    host="localhost",
    user="superc",
    password="superc",
    database="superc"
    )
cursor = conexion.cursor()

raiz = tk.Tk()
Style(theme='cosmo')
raiz.geometry("800x400")
raiz.columnconfigure(0, minsize=100)
raiz.columnconfigure(1, minsize=100)
raiz.columnconfigure(2, minsize=600)
raiz.rowconfigure(0, weight=1)

contienetablas = ttk.LabelFrame(
    raiz,
    text="Tablas en la BBDD",
    borderwidth=1,
    width=100,
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
    width=100,
    relief="ridge"
    )
contieneformulario.grid(row=0,column=1,sticky="nsew",padx=5,pady=5)
cursor.execute("SHOW COLUMNS IN productos")
columnas = cursor.fetchall()
for columna in columnas:  
    ttk.Label(contieneformulario,text=columna[0]).pack(padx=5,pady=5)
    ttk.Entry(contieneformulario).pack(padx=5,pady=5)

contienedatos = ttk.LabelFrame(
    raiz,
    text="Datos en mi sistema",
    borderwidth=1,
    width=600,
    relief="ridge"
    )
contienedatos.grid(row=0,column=2,sticky="nsew",padx=5,pady=5)
arbol = ttk.Treeview(contienedatos)
arbol['columns'] = ("nombre","apellidos",)
arbol.grid(row=0,column=0,padx=5,pady=5,sticky="nsew")
arbol.heading("#0",text="Columna 0")
arbol.heading("nombre",text="Nombre")
arbol.heading("apellidos",text="Apellidos")
arbol.column("#0",width=100)
arbol.column("nombre",width=100)
arbol.column("apellidos",width=100)

arbol.insert('','end',values=("Jose Vicente","Carratala"))
arbol.insert('','end',values=("Juan","Garcia"))
arbol.insert('','end',values=("Jorge","Lopez"))

arbol.bind('<Button-1>',clickEnArbol)

ttk.Button(contienedatos,text="Elimina el registro seleccionado",command=eliminaRegistro).grid(row=1,column=0,padx=5,pady=5,sticky="nsew")


raiz.mainloop()
