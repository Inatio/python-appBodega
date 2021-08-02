import tkinter as tk
import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#VentanaMain
def menu_pantalla():
    global pantalla
    pantalla = Tk()
    pantalla.geometry("300x400")
    pantalla.title("Bienvenidos")
    pantalla.iconbitmap("box.ico")

    #ImagenEncabezado
    image = PhotoImage(file = "box.gif")
    image = image.subsample(2,2)
    label = Label(image = image)
    label.pack()

    #ImagenDeFondo  
    fondo = PhotoImage(file = "caja.gif")
    labelFondo = Label(pantalla, image=fondo).place(x=0, y=0) 

    Label(text = "Bienvenido a Box", bg = "navy", fg = "white", width = "300", height = "3", font = ("calibri", 15)).pack()
    Label(text = "").pack()

    Button(text = "Iniciar Sesion", height = "3", width = "30", command = inicio_sesion).pack()
    Label(text = "").pack()
    Button(text = "Registrar Usuario", height = "3", width = "30", command = registrar).pack()
    Label(text = "").pack()
    Button(text = "Salir", height = "3", width = "30", command = cerrar_ventana).pack()
    Label(text = "").pack()

    pantalla.mainloop()

def cerrar_ventana():
    pantalla.destroy()

#VentanaInicioSesion
def inicio_sesion():
    global pantalla1
    pantalla1 = Toplevel (pantalla)
    pantalla1.geometry("400x250")
    pantalla1.title("Inicio de Sesion")
    pantalla1.iconbitmap("box.ico")

    #ImagenDeFondo  
    fondo = PhotoImage(file = "caja1.gif")
    labelFondo = Label(pantalla1, image=fondo).place(x=0, y=0) 

    Label(pantalla1, text = "Ingresar Usuario y Contraseña", bg = "navy", fg = "white", width = "300", height = "3", font = ("calibri", 15)).pack()
    Label(pantalla1, text = "").pack()

    global nombreusuario_verify
    global contrasenausuario_verify

    nombreusuario_verify = StringVar()
    contrasenausuario_verify = StringVar()

    global nombre_usuario_entry
    global contrasena_usuario_entry

    Label(pantalla1, text = "Usuario").pack()
    nombre_usuario_entry = Entry(pantalla1, textvariable = nombreusuario_verify)
    nombre_usuario_entry.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text = "Contraseña").pack()
    contrasena_usuario_entry = Entry(pantalla1, show="*" ,textvariable = contrasenausuario_verify)
    contrasena_usuario_entry.pack()
    Label(pantalla1).pack()

#BotonLogin
    Button(pantalla1, text = "Iniciar Sesion", command = validacion_datos).pack()

    pantalla1.mainloop()

#VentanaDeRegistro
def registrar():
    global pantalla2
    pantalla2 = Toplevel(pantalla)
    pantalla2.geometry("400x250")
    pantalla2.title("Registros")
    pantalla2.iconbitmap("box.ico")
    
    #Icono
    image = PhotoImage(file = "box.gif")
    image = image.subsample(2,2)
    label = Label(image = image)
    label.pack()

    #ImagenDeFondo  
    fondo = PhotoImage(file = "caja1.gif")
    labelFondo = Label(pantalla2, image=fondo).place(x=0, y=0)
    

    global nombreusuario_entry
    global contrasena_entry

    nombreusuario_entry = StringVar()
    contrasena_entry = StringVar()

    Label(pantalla2, text = "Registre un Usuario y Contraseña", bg = "navy", fg = "white", width = "300", height = "3", font = ("calibri", 15)).pack()
    Label(pantalla2, text ="").pack()

    Label(pantalla2, text = "Usuario").pack()
    nombreusuario_entry = Entry(pantalla2)
    nombreusuario_entry.pack()
    Label(pantalla2).pack()

    Label(pantalla2, text = "Contraseña").pack()
    contrasena_entry = Entry(pantalla2, show="*")
    contrasena_entry.pack()
    Label(pantalla2).pack()

#BotonRegistro
    Button(pantalla2, text = "Registrar", command=agregar_usuario).pack()

    pantalla2.mainloop()

#Ventana Registro de Objeto
def ingresar_objeto():
    global pantalla3
    pantalla3 = Toplevel(pantalla)
    pantalla3.geometry("350x500")
    pantalla3.title("Ventana de Registro Objetos")
    pantalla3.iconbitmap("box.ico")

    #ImagenDeFondo  
    fondo = PhotoImage(file = "caja2.gif")
    labelFondo = Label(pantalla3, image=fondo).place(x=0, y=0)

    global nombreproducto_entry
    global codigoproducto_entry
    global precioproducto_entry
    global marcaproducto_entry
    global numeroproducto_entry

    Label(pantalla3, text = "Nombre Producto").pack()
    nombreproducto_entry = Entry(pantalla3)
    nombreproducto_entry.pack()
    Label(pantalla3).pack()

    Label(pantalla3, text = "Codigo Producto").pack()
    codigoproducto_entry = Entry(pantalla3)
    codigoproducto_entry.pack()
    Label(pantalla3).pack()

    Label(pantalla3, text = "Precio Producto").pack()
    precioproducto_entry = Entry(pantalla3)
    precioproducto_entry.pack()
    Label(pantalla3).pack()

    Label(pantalla3, text = "Marca Producto").pack()
    marcaproducto_entry = Entry(pantalla3)
    marcaproducto_entry.pack()
    Label(pantalla3).pack()

    Label(pantalla3, text = "Numero Producto").pack()
    numeroproducto_entry = Entry(pantalla3)
    numeroproducto_entry.pack()
    Label(pantalla3).pack()

    #Botones
    boton1=tk.Button(pantalla3, text="Registrar", fg="black", command=registro_producto)
    boton1.pack(side=tk.LEFT)

    boton2=tk.Button(pantalla3, text="Lista", fg="black", command=listado)
    boton2.pack(side=tk.LEFT)

    boton3=tk.Button(pantalla3, text="Actualizar", fg="black", command=actualizar_producto)
    boton3.pack(side=tk.LEFT)

    boton4=tk.Button(pantalla3, text="Eliminar", fg="black", command=eliminar)
    boton4.pack(side=tk.LEFT)

    boton5=tk.Button(pantalla3, text="Salir", fg="black", command=cerrar_ventana)
    boton5.pack(side=tk.LEFT)

    pantalla3.mainloop()

def listado():
    global pantalla4
    pantalla4 = Toplevel(pantalla)
    pantalla4.geometry("350x500")
    pantalla4.title("Listado de Objetos")
    pantalla4.iconbitmap("box.ico")

   #ImagenDeFondo  
    fondo = PhotoImage(file = "caja3.gif")
    labelFondo = Label(pantalla4, image=fondo).place(x=0, y=0)

    #Tabla
    tree = ttk.Treeview(pantalla4, columns=(1), show="headling", height="6")
    tree.pack()

    tree.headling(1, Text="Nombre")
    tree.headling(2, Text="Producto")
    tree.headling(3, Text="Codigo")
    tree.headling(4, Text="Precio")
    tree.headling(5, Text="Marca")


def agregar_usuario():
    #ConexionBD
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="bd2"
    )
        
    fcursor=bd.cursor()

    sql = "INSERT INTO login (usuario, contrasena) VALUES ('{0}', '{1}')".format(nombreusuario_entry.get(), contrasena_entry.get())

    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Registro Exitoso", title = "Aviso")

    except:
        bd.rollback()
        messagebox.showinfo(message="No Registrado", title="Aviso")

    bd.close()


def validacion_datos():
    #ConexionBD
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="bd2"
    )
    
    fcursor=bd.cursor()

    fcursor.execute("SELECT contrasena FROM login WHERE usuario='"+nombreusuario_verify.get()+"'and contrasena='"+contrasenausuario_verify.get()+"'")

    if fcursor.fetchall():
        messagebox.showinfo(title="Inicio de Sesion Correcto", message="Usuario y Contraseña Correcto")
        ingresar_objeto()

    else:
        messagebox.showinfo(title="Inicio de Sesion Incorrecto", message="Usuario y Contraseña Incorrecto")
    
    bd.close()


def registro_producto():
    #ConexionBD
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="bd2"
    )

    fcursor=bd.cursor()

    sql = "INSERT INTO producto (nombreproducto, codigo, precio, marca, numero) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}' )".format(nombreproducto_entry.get(), codigoproducto_entry.get(), precioproducto_entry.get(), marcaproducto_entry.get(), numeroproducto_entry.get())

    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Registro Exitoso", title="Aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="Registro Fallido", title="Aviso")       

        bd.close()

def eliminar():
    #ConexionBD
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="bd2"
    )

    fcursor=bd.cursor()

    sql = "DELETE FROM producto WHERE nombreproducto='"+nombreproducto_entry.get()+"'"

    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Borrado Exitoso", title="Aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="Borrado Fallido", title="Aviso")       

        bd.close()

def actualizar_producto():
    #ConexionBD
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="bd2"
    )

    fcursor=bd.cursor()

    sql = "UPDATE producto SET nombreproducto = '"+nombreproducto_entry.get()+"', codigo='"+codigoproducto_entry.get()+"', precio='"+precioproducto_entry.get()+"', marca='"+marcaproducto_entry.get()+"', numero='"+numeroproducto_entry.get()+"' WHERE nombreproducto='"+nombreproducto_entry.get()+"' " 

    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Actualizacion Exitosa", title="Aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="Actualizacion Fallida", title="Aviso")       

        bd.close()

menu_pantalla()