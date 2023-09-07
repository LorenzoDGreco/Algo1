"""
Programa hecho por Revelacion, integrantes:
-Lorenzo Donato Greco
-Leandro Francisco Pereyra
-Cristobal Rodolfo Alvarez
-Federico Neuman
-Sebastián Kraglievich

Cuando usamos el icono sin la ruta completa tira error por no definido

Bibliografia del MessageBox
https://docs.python.org/3/library/tkinter.messagebox.html
"""
from tkinter import *
from tkinter import messagebox

COLOR_FONDO = "#46178f"
TAMANIO_INTERFAZ = "300x130"
NOMBRE_TITULO = "Login Revelacion"
ICONO = "icono.ico"

def login():
    """
    Arma la Interfaz Grafica del Ingreso de Usuarios
    """
    root = Tk()
    root.title(NOMBRE_TITULO)
    root.iconbitmap('D:\Descargas\Estudios\Python Progreso\Tareas\TareaGrupo\icono.ico')
    root.resizable(False, False)
    root.geometry(TAMANIO_INTERFAZ)
    root.config(bg=COLOR_FONDO)

    usuario = Label(text="Usuario Alumno:", fg="white", bg=COLOR_FONDO, font=15).place(x=15, y=15)
    contrasenia = Label(text="Clave:", fg="white", bg=COLOR_FONDO, font=15).place(x=15, y=45)

    casilla_usuario = Entry(root)
    casilla_usuario.place(x=150, y=15, width=130, height=20)

    casilla_contrasenia = Entry(root)
    casilla_contrasenia.config(show="*")
    casilla_contrasenia.place(x=150, y=45, width=130, height=20)

    boton_verificar = Button(root, text="Ingresar",command= lambda :verificar_usuario(obtener_usuarios_claves(casilla_usuario, casilla_contrasenia)))

    boton_verificar.place(x=165, y=80)

    root.mainloop()

def verificar_usuario(diccionario_ingresado):
    """
    Valida que el Usuario y la Clave ingresada sean correctos
    """
    diccionario_valido = {"Greco":"PVoRTN", "Neuman":"essupersecreta", "Pereyra":"perro", "Alvarez":"Clavel", "Kraglievich":"LaDelCampus"}

    usuario_ingresado = list(diccionario_ingresado.keys())[0]
    contrasenia_ingresada = diccionario_ingresado[usuario_ingresado]

    if (usuario_ingresado in diccionario_valido.keys()) and (contrasenia_ingresada == diccionario_valido[usuario_ingresado]):
        messagebox.showinfo("Login Revelacion", "Usuario y Clave Correctos")
    else:
        messagebox.showerror("Login Revelacion", "Algunos de los datos ingresados es Incorrecto")

def obtener_usuarios_claves(casilla_usuario, casilla_contrasenia):
    """
    Arma y retorna un diccionario con los datos ingresados del Usuario
    """
    diccionario_ingresado = {casilla_usuario.get():casilla_contrasenia.get()}
    return diccionario_ingresado


login()