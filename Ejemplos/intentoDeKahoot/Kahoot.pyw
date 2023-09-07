from tkinter import *
from functools import partial
from tkinter import ttk

# Variables globales, no deberían de serlo pero no se me ocurre como hacelo bien jeje
lista_partida = []
max_partidas_guardadas = 0
pregunta_actual = 0
puntos = 0
# Posiciones estaticas de la lista
NOMBRES = 0
BOOLEANOS = 1
NOMBRE_PREGUNTA = 0
NOMBRE_BOTON_ROJO = 1
NOMBRE_BOTON_AZUL = 2
NOMBRE_BOTON_AMARILLO = 3
NOMBRE_BOTON_VERDE = 4
BOOLEAN_ROJO = 0
BOOLEAN_AZUL = 1
BOOLEAN_AMARILLO = 2
BOOLEAN_VERDE = 3

def setup(root):
    root.title("Kahoot!")
    root.resizable(False, False)
    root.iconbitmap("icono.ico")
    root.geometry("650x400")
    canvas = Canvas(width=650, height=400, bg="#46178f")
    canvas.pack()
    canvas.create_rectangle(10, 10, 200, 200, width=5,
                            fill="#3f1581", outline="")
    canvas.create_oval(350, 150, 700, 500,
                       fill="#3f1581", outline="")
    root.config(bg="#46178f")
    label_inicio = Label(text="Kahoot!", fg="white", bg="#46178f", font=(
        "Noto Sans Arabic", 18)).place(x=300, y=125)
    boton_Crear = Button(root, text=" Crear Partida",
                         command=partial(crear_partida, root))
    boton_Crear.place(x=305, y=180)
    boton_Jugar = Button(root, text="Iniciar partida",
                         command=partial(jugar_partida, root))
    boton_Jugar.place(x=305, y=220)

def crear_partida(root):
    root.destroy()
    menu_crear_partida()

def jugar_partida(root):
    if not lista_partida == []:
        root.destroy()
        interfaz_juego()
    else:
        label_aviso = Label(root, text="Primero necesitas crear las preguntas!", fg="red", bg="#46178f", font=(
                            "Noto Sans Arabic", 11)).place(x=10, y=370)

def menu_crear_partida():
    root1 = Tk()
    root1.title("Kahoot!")
    root1.resizable(False, False)
    root1.iconbitmap(
        "icono.ico")
    root1.geometry("650x400")
    canvas = Canvas(width=650, height=400, bg="#46178f")
    canvas.pack()
    canvas.create_rectangle(10, 10, 200, 200, width=5,
                            fill="#3f1581", outline="")
    canvas.create_oval(350, 150, 700, 500,
                       fill="#3f1581", outline="")
    root1.config(bg="#46178f")

    check_rojo = IntVar()
    check_azul = IntVar()
    check_amarillo = IntVar()
    check_verde = IntVar()

    label_pregunta = Label(text="Ingrese la pregunta", fg="white", bg="#46178f", font=(
        "Noto Sans Arabic", 18)).place(x=250, y=70)

    texto_pregunta = Entry(root1)
    texto_pregunta.place(x=200, y=100, width=300, height=20)
    texto_respuesta_1 = Entry()
    texto_respuesta_1.place(x=100, y=200, width=200, height=20)
    texto_respuesta_2 = Entry(root1)
    texto_respuesta_2.place(x=400, y=200, width=200, height=20)
    texto_respuesta_3 = Entry(root1)
    texto_respuesta_3.place(x=100, y=280, width=200, height=20)
    texto_respuesta_4 = Entry(root1)
    texto_respuesta_4.place(x=400, y=280, width=200, height=20)

    boton_Guardar = Button(root1, text="Confirmar cambios",
                           command=partial(guardar_partida, root1, texto_pregunta, texto_respuesta_1, texto_respuesta_2, texto_respuesta_3, texto_respuesta_4,
                                           check_rojo, check_azul, check_amarillo, check_verde))
    boton_Guardar.place(x=500, y=340)

    boton_Cancelar = Button(root1, text="Volver atras",
                            command=partial(cancelar_partida, root1))
    boton_Cancelar.place(x=420, y=340)

    check_boton_1 = Checkbutton(root1, text="rojo", variable=check_rojo,
                                bg="#46178f", fg="red", font=11)
    check_boton_1.place(x=100, y=230)

    check_boton_2 = Checkbutton(root1, text="azul", variable=check_azul,
                                bg="#3f1581", fg="blue", font=11)
    check_boton_2.place(x=400, y=230)

    check_boton_3 = Checkbutton(root1, text="amarillo", variable=check_amarillo,
                                bg="#46178f", fg="orange", font=11)
    check_boton_3.place(x=100, y=310)

    check_boton_4 = Checkbutton(root1, text="verde", variable=check_verde,
                                bg="#3f1581", fg="green", font=11)
    check_boton_4.place(x=400, y=310)

    canvas.create_rectangle(75, 200, 100, 221, width=5,
                            fill="red", outline="")
    canvas.create_rectangle(375, 200, 400, 221, width=5,
                            fill="blue", outline="")
    canvas.create_rectangle(75, 280, 100, 300, width=5,
                            fill="yellow", outline="")
    canvas.create_rectangle(375, 280, 400, 300, width=5,
                            fill="green", outline="")

    root1.mainloop()

def guardar_partida(root1, texto_pregunta, texto_respuesta_1, texto_respuesta_2, texto_respuesta_3, texto_respuesta_4,
                    check_rojo, check_azul, check_amarillo, check_verde):

    global lista_partida, max_partidas_guardadas
    faltan_condiciones = False

    lista_caracteres = [len(texto_pregunta.get()), len(texto_respuesta_1.get()), len(
        texto_respuesta_2.get()), len(texto_respuesta_3.get()), len(texto_respuesta_4.get())]

    lista_texto = [texto_pregunta.get(), texto_respuesta_1.get(),
                   texto_respuesta_2.get(), texto_respuesta_3.get(), texto_respuesta_4.get()]
    lista_booleanos = [check_rojo.get(), check_azul.get(),
                       check_amarillo.get(), check_verde.get()]

    if 0 in lista_caracteres:
        label_notificacion = Label(text="Completa todos los campos para continuar", fg="red", bg="#46178f", font=(
            "Noto Sans Arabic", 11)).place(x=10, y=370)
        faltan_condiciones = True
    else:
        for elemento in lista_caracteres:
            if elemento > 32:
                label_notificacion = Label(text="Ingrese menos de 32 caracteres\t\t", fg="red", bg="#46178f", font=(
                    "Noto Sans Arabic", 11)).place(x=10, y=370)
                faltan_condiciones = True

    if not faltan_condiciones:
        if max_partidas_guardadas < 10:
            max_partidas_guardadas += 1
            lista_intermedia = []
            lista_intermedia.append(lista_texto)
            lista_intermedia.append(lista_booleanos)
            lista_partida.append(lista_intermedia)
            label_notificacion = Label(text="Se guardó la pregunta n°" + str(max_partidas_guardadas) + "\t\t", fg="green", bg="#46178f", font=(
                "Noto Sans Arabic", 11)).place(x=10, y=370)
            print(lista_partida)
            print(max_partidas_guardadas)

def cancelar_partida(root1):
    root1.destroy()
    main()

def interfaz_juego():

    root2 = Tk()
    root2.title("Kahoot!")
    root2.resizable(False, False)
    root2.iconbitmap("icono.ico")
    root2.config(bg="#46178f")
    root2.geometry("650x400")
    canvas = Canvas(width=650, height=400, bg="#46178f")
    canvas.pack()

    canvas.create_rectangle(75, 200, 100, 221, width=5,
                            fill="red", outline="")
    canvas.create_rectangle(375, 200, 400, 221, width=5,
                            fill="blue", outline="")
    canvas.create_rectangle(75, 280, 100, 300, width=5,
                            fill="yellow", outline="")
    canvas.create_rectangle(375, 280, 400, 300, width=5,
                            fill="green", outline="")

    graficar_nueva_pregunta(root2)
    print("son iguales? ", pregunta_actual, max_partidas_guardadas)

    root2.mainloop()

def graficar_nueva_pregunta(root2):


    label_notificacion = Label(root2, text=lista_partida[pregunta_actual][NOMBRES][NOMBRE_PREGUNTA], fg="white", bg="#46178f", font=(
        "Noto Sans Arabic", 20))
    label_notificacion.place(x=650/3, y=100)

    boton_rojo = Button(root2, text=lista_partida[pregunta_actual][NOMBRES][NOMBRE_BOTON_ROJO] + "\t\t", font = (11),
                        command=partial(boton_respuesta, root2, label_notificacion, BOOLEAN_ROJO))
    boton_rojo.place(x=100, y=200, width=200, height=20)

    boton_azul = Button(root2, text=lista_partida[pregunta_actual][NOMBRES][NOMBRE_BOTON_AZUL] + "\t\t", font = (11),
                        command=partial(boton_respuesta, root2, label_notificacion, BOOLEAN_AZUL))
    boton_azul.place(x=400, y=200, width=200, height=20)

    boton_amarillo = Button(root2, text=lista_partida[pregunta_actual][NOMBRES][NOMBRE_BOTON_AMARILLO] + "\t\t", font = (11),
                            command=partial(boton_respuesta, root2, label_notificacion, BOOLEAN_AMARILLO))
    boton_amarillo.place(x=100, y=280, width=200, height=20)

    boton_verde = Button(root2, text=lista_partida[pregunta_actual][NOMBRES][NOMBRE_BOTON_VERDE] + "\t\t", font = (11),
                         command=partial(boton_respuesta, root2, label_notificacion, BOOLEAN_VERDE))
    boton_verde.place(x=400, y=280, width=200, height=20)

def boton_respuesta(root2, label_notificacion, constante):
    global pregunta_actual, puntos
    
    if pregunta_actual < max_partidas_guardadas:
        
        print(max_partidas_guardadas)
        print(pregunta_actual)
        label_notificacion.destroy()
        if lista_partida[pregunta_actual][BOOLEANOS][constante] == 1:
            puntos += 1
            label_puntos = Label(root2, text="Muy buen, seleccionaste la correcta, sigue así! Tus puntos son: " + str(puntos) + "\t\t", 
                                fg="white", bg="#46178f", font=("Noto Sans Arabic", 11)).place(x=650/10, y=40)
        else:
            label_puntos = Label(root2, text="Seleccionaste la incorrecta, suerte para la proxima! Tus puntos son: " + str(puntos) + "\t\t", 
                                fg="white", bg="#46178f", font=("Noto Sans Arabic", 11)).place(x=650/10, y=40)        
    pregunta_actual += 1

    if pregunta_actual == max_partidas_guardadas:
        print("puntaje total: ", puntos)
        root2.destroy()
        pantalla_fin()

    
    graficar_nueva_pregunta(root2)

def pantalla_fin():
    color_podio = ""
    texto_label = ""
    root3 = Tk()
    root3.title("Kahoot!")
    root3.resizable(False, False)
    root3.iconbitmap("icono.ico")
    root3.config(bg="#46178f")
    root3.geometry("650x400")

    canvas = Canvas(width=650, height=400, bg="#46178f")
    canvas.pack()
    
    if(puntos == max_partidas_guardadas):
        color_podio = "#D4AF37"
        texto_label = "         Felicidades has respondido todas bien,\n   has sacado la medalla de oro!\n  Tu puntaje: " + str(puntos)

    elif(puntos > max_partidas_guardadas/2):
        color_podio = "#C0C0C0"
        texto_label = "         Muy bien, has resondido la mayoría bien,\n   has sacado la medalla de plata!\n  Tu puntaje: " + str(puntos)
    else:
        color_podio = "#8B511C"
        texto_label = "Suerte para la proxima,\n has respondido incorrectamente varias preguntas,\n has sacado la medalla de bronce!\n Tu puntaje: " + str(puntos)

    canvas.create_rectangle(200, 200, 450, 400, width=5,
                            fill=color_podio, outline="")
    label_puntos = Label(root3, text=texto_label, 
                                fg=color_podio, bg="#46178f", font=("Noto Sans Arabic", 20)).place(x=25, y=40) 
    root3.mainloop()

def main():
    root = Tk()
    setup(root)
    root.mainloop()

main()