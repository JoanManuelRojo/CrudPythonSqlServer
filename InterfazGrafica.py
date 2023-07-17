# Se importan los paquetes

from tkinter import *
from tkinter import messagebox
import sqlServerCon


# Se declaran las propiedades de tkinter

root =Tk()

miFrame = Frame(root, width=500, height=400)
miFrame.pack()

# Variables

miNombre=StringVar()
varOpcion=IntVar()

# Botones y funciones

# Botón confirmar alta le pasa los atributos declarados en los campos que el usuario puede escribir y envia a la base de datos la consulta para su registro.
def botonConfirmarAlta():
    id = entradaId.get()
    nombre = entradaNombre.get()
    clave = entradaClave.get()
    apellido = entradaApellido.get()
    direccion = entradaDireccion.get()
    comentarios = entradaComentarios.get("1.0", "end-1c")

    # Se crea la conexión a la base de datos dentro de la función

    conexion_bdd = sqlServerCon.sqlServerCon()

    # Acá llama al método crearUsuario de la clase sqlServerCon

    conexion_bdd.crearUsuario(id, nombre, clave, apellido, direccion, comentarios)

    messagebox.showinfo("Registro", "Se creó correctamente el usuario en la base de datos.")


    # Acá se vacían los campos de entrada de datos después de la operación

    entradaId.delete(0, "end")
    miNombre.set("")
    entradaClave.delete(0, "end")
    entradaApellido.delete(0, "end")
    entradaDireccion.delete(0, "end")
    entradaComentarios.delete("1.0", "end")


def botonConfirmarBaja():

    # Acá se vacían los campos de entrada de datos después de la operación

    entradaId.delete(0, "end")
    miNombre.set("")
    entradaClave.delete(0, "end")
    entradaApellido.delete(0, "end")
    entradaDireccion.delete(0, "end")
    entradaComentarios.delete("1.0", "end")

def botonConfirmarModificar():
    pass

def botonConfirmarConsulta():

    id = entradaId.get()

    # Se crea la conexión a la base de datos dentro de la función

    conexion_bdd = sqlServerCon.sqlServerCon()

    # Acá llama al método crearUsuario de la clase sqlServerCon

    conexion_bdd.mostrarUsuario(id)

    # Acá se vacían los campos de entrada de datos después de la operación

    entradaNombre.insert()
    entradaClave.insert()
    entradaApellido.insert()
    entradaDireccion.insert()
    entradaComentarios.insert()

def botonConfirmar():
    pass

botonConfirmar=Button(root, text="Confirmar", command=botonConfirmarAlta)
botonConfirmar.pack()


def botonLimpiar():
    entradaId.delete(0, "end")
    miNombre.set("")
    entradaClave.delete(0, "end")
    entradaApellido.delete(0, "end")
    entradaDireccion.delete(0, "end")
    entradaComentarios.delete("1.0", "end")



def funcionSalir():
    salir = messagebox.askquestion("Salir","¿Seguro que quieres salir?")
    if salir == "yes":
        root.destroy()


def funcionAcerca():
    messagebox.showinfo("Joan Manuel Rojo", "Crud realizado para el parcial 2 de Programación Aplicada."
    )

def funcionLicencia():
    messagebox.showinfo("Licencia", "Uso libre."
    )

# Menú

def infoAdicional():
    messagebox.showinfo("Editar")


barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

datosM=Menu(barraMenu, tearoff=0)
datosM.add_command(label="Salir", command=funcionSalir)


crudM=Menu(barraMenu, tearoff=0)
crudM.add_command(label="Alta")
crudM.add_command(label="Baja")
crudM.add_command(label="Modificación")
crudM.add_command(label="Consulta")


ayudaM=Menu(barraMenu, tearoff=0)
ayudaM.add_command(label="Licencia", command=funcionLicencia)
ayudaM.add_command(label="Acerca de...", command=funcionAcerca)

barraMenu.add_cascade(label="Archivo", menu=datosM)
barraMenu.add_cascade(label="Limpiar", menu='?', command=botonLimpiar)
barraMenu.add_cascade(label="ABCM", menu=crudM)
barraMenu.add_cascade(label="Ayuda", menu=ayudaM)

# Ingreso de textos

entradaId=Entry(miFrame)
entradaId.grid(row=0, column=1, padx=10, pady=10)

entradaNombre=Entry(miFrame, textvariable=miNombre)
entradaNombre.grid(row=3, column=1, padx=10, pady=10)

entradaClave=Entry(miFrame)
entradaClave.grid(row=4, column=1, padx=10, pady=10)
entradaClave.configure(show="?")

entradaApellido=Entry(miFrame)
entradaApellido.grid(row=5, column=1, padx=10, pady=10)

entradaDireccion=Entry(miFrame)
entradaDireccion.grid(row=6, column=1, padx=10, pady=10)

entradaComentarios=Text(miFrame, width=16, height=5)
entradaComentarios.grid(row=7, column=1, padx=10, pady=10)

# Choise
labelId = Label(miFrame, text="GÉNERO: ")
labelId.grid(row=1, column=0, padx=10, pady=10)

opcionMasc = Radiobutton(miFrame, text="Masculino", variable=varOpcion, value=1)
opcionMasc.grid(row=1, column=1, padx=10, pady=10)

opcionFem = Radiobutton(miFrame, text="Femenino", variable=varOpcion, value=2)
opcionFem.grid(row=2, column=1, padx=10, pady=10)


# Barra de desplazamiento

scrollVert=Scrollbar(miFrame, command=entradaComentarios.yview)
scrollVert.grid(row=7, column=2, sticky="nsew")

entradaComentarios.config(yscrollcommand=scrollVert.set)


# Labels

labelId = Label(miFrame, text="ID: ")
labelId.grid(row=0, column=0, padx=10, pady=10)

labelNombre = Label(miFrame, text="NOMBRE: ")
labelNombre.grid(row=3, column=0, padx=10, pady=10)

labelClave = Label(miFrame, text="CONTRASEÑA: ")
labelClave.grid(row=4, column=0, padx=10, pady=10)

labelApellido = Label(miFrame, text="APELLIDO: ")
labelApellido.grid(row=5, column=0, padx=10, pady=10)

labelDireccion = Label(miFrame, text="DIRECCIÓN: ")
labelDireccion.grid(row=6, column=0, padx=10, pady=10)

labelComentarios = Label(miFrame, text="COMENTARIO: ")
labelComentarios.grid(row=7, column=0, padx=10, pady=10)


root.mainloop()