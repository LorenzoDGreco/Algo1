# ------------------------ Importación de librerías ------------------------ #
# Python / Externas
import doctest
import tkinter as tk
from tkinter import messagebox

# Internas
from constantes_interfaz import (
                                 COLOR_DE_LETRAS_PRINCIPAL,
                                 COLOR_DE_FONDO_DE_BOTONES,
                                 COLOR_DE_FONDO_DE_VENTANAS,
                                 COLOR_DE_FONDO_DE_CASILLAS_DE_TEXTO,
                                 COLOR_DE_FONDO_DE_ETIQUETAS,
                                 TIPO_TEXTO_DE_FUENTE,
                                 FUENTE,
                                 SEPARACION_DE_ACCESORIOS,
                                 TIPO_DE_BORDE_DE_BOTONES,
                                 TIPO_DE_CURSOR_SOBRE_BOTONES,
                                 TIPO_DE_CURSOR_BOTON_CANCELAR,
                                 GROSOR_DE_BORDE_BOTONES,
                                 ANCHO_BOTON,
                                 CANTIDAD_MIN_CARACTERES_CONTRASENIA,
                                 CANTIDAD_MAX_CARACTERES_CONTRASENIA,
                                 CANTIDAD_MIN_CARACTERES_USUARIO,
                                 CANTIDAD_MAX_CARACTERES_USUARIO,
                                 LETRAS_ACENTUADAS,
                                 REGISTROS_DE_CUENTAS,
                                 MENSAJE_CONTRASENIA_INCORRECTA,
                                 MENSAJE_ERROR_INGRESO,
                                 MENSAJE_MAXIMO_INGRESO,
                                 MENSAJE_CERRAR,
                                 VENTANA_EMERGENTE_SALIR,
                                 IMAGEN_GRUPO,
                                 IMAGEN_JUEGO
                                )

from constantes_de_texto import CODIFICACION

# -------------------- Definición de funciones propias --------------------- #

def traer_registro_de_cuentas():
    """
    Lee un archivo y arma un diccionario que contiene como clave los usuarios
    y como valor su respectiva contraseña.
    Post: Retorna un diccionario con el contenido del archivo.
    """
    cuentas_registradas = {}
    try:
        with open(REGISTROS_DE_CUENTAS, "r", encoding=CODIFICACION) as archivo:
            for linea in archivo:
                nombre_registrado, contrasenia_registrada = linea.rstrip().split(',')
                if not nombre_registrado in cuentas_registradas.keys():
                    cuentas_registradas[nombre_registrado] = contrasenia_registrada

    except FileNotFoundError:
        with open(REGISTROS_DE_CUENTAS, "w", encoding=CODIFICACION) as archivo:
            pass

    return cuentas_registradas

def configurar_raiz(raiz, titulo, icono, dimensionable="ninguno"):
    """
    Configura el aspecto y las propiedades de la raiz enviada por parámetro
    con los valores del resto de parámetros.
    """
    raiz.title(titulo)
    raiz.iconbitmap(f"iconos\\{icono}")
    raiz.config(bg=COLOR_DE_FONDO_DE_VENTANAS)
    raiz.state("normal")
    raiz.rowconfigure(0, weight=1)
    raiz.rowconfigure(1, weight=1)
    raiz.rowconfigure(2, weight=1)
    raiz.columnconfigure(0, weight=1)
    raiz.columnconfigure(1, weight=1)
    raiz.columnconfigure(2, weight=4)
    if (dimensionable == "ninguno"):
        raiz.resizable(False, False)
    elif (dimensionable == "ambos"):
        raiz.resizable(True, True)
    elif (dimensionable == "x"):
        raiz.resizable(True, False)
    elif (dimensionable == "y"):
        raiz.resizable(False, True)

def instanciar_etiquetas_de_imagen_interfaz_principal(contenedor, imagen_grupo, imagen_juego):
    """
    Instancia todas las etiquetas, de la interfaz principal, que contienen
    imagenes y las configura.
    """
    # - Etiqueta de imagen del grupo revelación - #
    etiqueta_imagen_revelacion = tk.Label(contenedor, image=imagen_grupo)
    configurar_etiqueta(etiqueta_imagen_revelacion, fila=1, columna=0)

    # - Etiqueta de imagen del juego - #
    etiqueta_imagen_ahorcado = tk.Label(contenedor, image=imagen_juego)
    configurar_etiqueta(etiqueta_imagen_ahorcado, fila=1, columna=2)

def configurar_etiqueta(etiqueta, fila, columna, varias_columnas=1, orientacion="", fuente=FUENTE, separacion_interna=(0, 0)):
    """
    Configura el aspecto de la etiqueta enviada por parámetro con los valores
    del resto de parámetros.
    Pre: -fila: Debe ser un número entero positivo o 0.
         -columna: Debe ser un número entero positivo o 0.
         -varias_columnas: Debe ser un número entero positivo o 0.
    """
    HORIZONTAL = 0
    VERTICAL = 1
    etiqueta.config(
                    bg=COLOR_DE_FONDO_DE_ETIQUETAS,
                    fg=COLOR_DE_LETRAS_PRINCIPAL,
                    font=fuente,
                    justify="center"
                   )
    etiqueta.grid(
                  row=fila,
                  column=columna,
                  columnspan=varias_columnas,
                  sticky=orientacion,
                  ipadx=separacion_interna[HORIZONTAL],
                  ipady=separacion_interna[VERTICAL],
                  pady=SEPARACION_DE_ACCESORIOS,
                  padx=SEPARACION_DE_ACCESORIOS
                 )

def configurar_frame(frame, ubicacion_grilla=(None, None)):
    """
    Configura el aspecto del frame enviado por parámetro con los valores
    del resto de parámetros.
    Pre: -ubicacion_grilla: Debe ser un tipo de dato al que se accede por
                            subindice.
    """
    FILA = ubicacion_grilla[0]
    COLUMNA = ubicacion_grilla[1]

    if (FILA != None) and (COLUMNA != None):
        frame.grid(row=FILA, column=COLUMNA)
    else:
        frame.pack()
    
    frame.config(bg=COLOR_DE_FONDO_DE_VENTANAS)

def instanciar_etiquetas_interfaz_principal(frame_de_opciones):
    """
    Instancia todas las etiquetas, de la interfaz principal, que contienen
    texto y las configura.
    """
    # - Etiqueta 'AHORCADO - REVELACIÓN' - #
    titulo = tk.Label(
                      frame_de_opciones,
                      text="AHORCADO - REVELACIÓN"
                     )
    configurar_etiqueta(
                        titulo,
                        fila=0,
                        columna=0,
                        fuente=(TIPO_TEXTO_DE_FUENTE, 18)
                       )
    
    # - Etiqueta 'MENÚ DE OPCIONES:' - #
    etiqueta_menu = tk.Label(
                             frame_de_opciones,
                             text="MENÚ DE OPCIONES:"
                            )
    configurar_etiqueta(
                        etiqueta_menu,
                        fila=1,
                        columna=0,
                        fuente=(TIPO_TEXTO_DE_FUENTE, 18)
                       )

def instanciar_botones_interfaz_principal(frame_de_opciones, listado_de_jugadores, numero_max_jugadores, cuentas_registradas, raiz):
    """
    Instancia todos los botones de la interfaz principal y los configura.
    """
    # - Botón 'Ingresar' - #
    boton_ingresar = tk.Button(
                               frame_de_opciones,
                               text='Ingresar',
                               width=ANCHO_BOTON,
                               command=lambda: ejecutar_interfaz_de_ingreso(
                                                                            boton_ingresar,
                                                                            listado_de_jugadores,
                                                                            numero_max_jugadores,
                                                                            cuentas_registradas
                                                                           )
                              )
    configurar_boton(boton_ingresar, fila=2, columna=0)

    # - Botón 'Registrar' - #
    boton_registrar = tk.Button(
                                frame_de_opciones,
                                text='Registrar',
                                width=ANCHO_BOTON,
                                command=lambda: ejecutar_interfaz_de_registro(
                                                                              boton_registrar,
                                                                              cuentas_registradas
                                                                             )
                               )
    configurar_boton(boton_registrar, fila=3, columna=0)

    # - Botón 'Iniciar partida' - #
    boton_iniciar = tk.Button(
                              frame_de_opciones,
                              text='Iniciar partida',
                              width=ANCHO_BOTON,
                              command=lambda: destruir_interfaz(
                                                                raiz,
                                                                boton_iniciar,
                                                                listado_de_jugadores
                                                               )
                             )
    configurar_boton(boton_iniciar, fila=4, columna=0)

    # - Botón 'Salir' - #
    boton_salir = tk.Button(
                            frame_de_opciones,
                            text='Salir',
                            width=ANCHO_BOTON,
                            command=lambda: destruir_interfaz(
                                                              raiz,
                                                              boton_salir,
                                                              listado_de_jugadores
                                                             )
                           )
    configurar_boton(boton_salir, fila=5, columna=0)

def configurar_boton(boton, fila, columna):
    """
    Configura el aspecto del botón enviado por parámetro con los valores
    del resto de parámetros.
    Pre: -fila: Debe ser un número entero positivo o 0.
         -columna: Debe ser un número entero positivo o 0.
    """
    if boton["text"] in ("Salir", "Volver"):
        boton.config(
                     bg=COLOR_DE_FONDO_DE_BOTONES,
                     font=FUENTE,
                     fg=COLOR_DE_LETRAS_PRINCIPAL,
                     bd=GROSOR_DE_BORDE_BOTONES,
                     relief=TIPO_DE_BORDE_DE_BOTONES,
                     cursor=TIPO_DE_CURSOR_BOTON_CANCELAR,
                     activebackground=COLOR_DE_LETRAS_PRINCIPAL,
                     activeforeground=COLOR_DE_FONDO_DE_BOTONES
                    )
    elif boton["text"] in ("Ingresar", "Registrar", "Iniciar partida"):
        boton.config(
                      bg=COLOR_DE_FONDO_DE_BOTONES,
                      font=FUENTE,
                      fg=COLOR_DE_LETRAS_PRINCIPAL,
                      bd=GROSOR_DE_BORDE_BOTONES,
                      relief=TIPO_DE_BORDE_DE_BOTONES,
                      cursor=TIPO_DE_CURSOR_SOBRE_BOTONES,
                      activebackground=COLOR_DE_LETRAS_PRINCIPAL,
                      activeforeground=COLOR_DE_FONDO_DE_BOTONES
                    )
    else:
        boton.config(
                      bg=COLOR_DE_FONDO_DE_BOTONES,
                      bd=GROSOR_DE_BORDE_BOTONES,
                      cursor=TIPO_DE_CURSOR_SOBRE_BOTONES,
                      activebackground=COLOR_DE_LETRAS_PRINCIPAL,
                      activeforeground=COLOR_DE_FONDO_DE_BOTONES
                    )
    boton.grid(
               row=fila,
               column=columna,
               pady=SEPARACION_DE_ACCESORIOS,
               padx=SEPARACION_DE_ACCESORIOS
              )

def ejecutar_interfaz_de_ingreso(boton_externo, listado_de_jugadores, numero_max_jugadores, cuentas_registradas):
    """
    Ejecuta la interfaz de ingreso.
    """
    boton_externo["state"] = "disabled"

    # - Raíz de ingreso - #
    raiz_de_ingreso = tk.Tk()
    configurar_raiz(
                    raiz_de_ingreso,
                    titulo="Ingreso de jugador",
                    icono="usuario.ico"
                   )

    # - Frame de ingreso - #
    frame_de_ingreso = tk.Frame(raiz_de_ingreso)
    configurar_frame(frame_de_ingreso)

    instanciar_etiquetas_interfaz_ingreso(frame_de_ingreso)

    # - Campo de texto de nombre de usuario - #
    casilla_nombre_de_usuario = instanciar_campo_de_texto(frame_de_ingreso, ubicacion_grilla=(1, 1))

    # - Campo de texto de contraseña - #
    casilla_contrasenia = instanciar_campo_de_texto(frame_de_ingreso, ubicacion_grilla=(2, 1), caracter_a_exhibir="*")

    # - Botón de chequeo (para mostrar contraseña) - #
    instanciar_boton_chequeo(frame_de_ingreso, casilla_contrasenia, ubicacion_grilla=(2, 2))

    # - Etiqueta identificadora variable - #
    etiqueta_variable = instanciar_etiqueta_variable(frame_de_ingreso, ubicacion_grilla=(4, 0), cantidad_columnas=2)

    instanciar_botones_interfaz_ingreso(
                                        frame_de_ingreso,
                                        etiqueta_variable,
                                        casilla_nombre_de_usuario,
                                        casilla_contrasenia,
                                        listado_de_jugadores,
                                        cuentas_registradas,
                                        numero_max_jugadores,
                                        raiz_de_ingreso,
                                        boton_externo
                                       )

    raiz_de_ingreso.protocol('WM_DELETE_WINDOW',
                             func=lambda: destruir_interfaz(
                                                            raiz_de_ingreso,
                                                            boton_externo,
                                                            listado_de_jugadores
                                                           )
                            )

    raiz_de_ingreso.mainloop()

def instanciar_etiquetas_interfaz_ingreso(frame_de_ingreso):
    """
    Instancia todas las etiquetas, de la interfaz de ingreso, que tendrán un
    texto constante y las configura.
    """
    # - Etiqueta 'Ingreso de usuario' - #
    etiqueta_titulo_ingreso = tk.Label(frame_de_ingreso, text="Ingreso de usuario")
    configurar_etiqueta(etiqueta_titulo_ingreso, fila=0, columna=0, varias_columnas=2, fuente=(TIPO_TEXTO_DE_FUENTE, 18))

    # - Etiqueta 'Nombre de usuario:' - #
    etiqueta_nombre = tk.Label(frame_de_ingreso, text="Nombre de usuario:")
    configurar_etiqueta(etiqueta_nombre, fila=1, columna=0, orientacion="e")
    
    # - Etiqueta 'Contraseña:' - #
    etiqueta_contrasenia = tk.Label(frame_de_ingreso, text="Contraseña:")
    configurar_etiqueta(etiqueta_contrasenia, fila=2, columna=0, orientacion="e")

def instanciar_campo_de_texto(contenedor, ubicacion_grilla=(None, None), caracter_a_exhibir=""):
    """
    Instancia la clase 'Entry' (del módulo tkinter) y la configura con los
    parámetros enviados.
    Pre: -ubicacion_grilla: Debe ser un tipo de dato al que se accede por
                            subindice.
    Post: Retorna el objeto instanciado.
    """
    FILA = ubicacion_grilla[0]
    COLUMNA = ubicacion_grilla[1]

    casilla = tk.Entry(contenedor)
    configurar_casilla_de_texto(casilla, fila=FILA, columna=COLUMNA, caracter_a_mostrar=caracter_a_exhibir)

    return casilla

def configurar_casilla_de_texto(casilla, fila, columna, caracter_a_mostrar=""):
    """
    Configura el aspecto de la casilla de texto enviada por parámetro con los
    valores del resto de parámetros.
    """
    casilla.config(
                   bg=COLOR_DE_FONDO_DE_CASILLAS_DE_TEXTO,
                   fg=COLOR_DE_LETRAS_PRINCIPAL,
                   justify="center",
                   show=caracter_a_mostrar
                  )
    casilla.grid(
                 row=fila,
                 column=columna,
                 pady=SEPARACION_DE_ACCESORIOS,
                 padx=SEPARACION_DE_ACCESORIOS
                )

def instanciar_boton_chequeo(contenedor, casilla_contrasenia, ubicacion_grilla=(None, None)):
    """
    Instancia la clase 'Checkbutton' (del módulo tkinter) y la configura con los
    parámetros enviados.
    Pre: -ubicacion_grilla: Debe ser un tipo de dato al que se accede por
                            subindice.
    """
    FILA = ubicacion_grilla[0]
    COLUMNA = ubicacion_grilla[1]
    
    boton_de_chequeo = tk.Checkbutton(contenedor, command=lambda: ocultar_contrasenia(casilla_contrasenia))
    configurar_boton(boton_de_chequeo, fila=FILA, columna=COLUMNA) 

def ocultar_contrasenia(casilla_contrasenia):
    """
    Cambia el caracter que se muestra al escribir en la casilla enviada por
    parámetro.
    Pre: -casilla_contrasenia: Debe ser una instancia de la clase 'Entry'
                               (del módulo tkinter).
    """
    if (casilla_contrasenia.cget('show') == ''):
        casilla_contrasenia.config(show='*')
    else:
        casilla_contrasenia.config(show='')

def instanciar_etiqueta_variable(contenedor, ubicacion_grilla=(None, None), cantidad_columnas=1):
    """
    Instancia la clase 'Label' (del módulo tkinter) y la configura con los
    parámetros enviados.
    Pre: -ubicacion_grilla: Debe ser un tipo de dato al que se accede por
                            subindice.
    """
    
    FILA = ubicacion_grilla[0]
    COLUMNA = ubicacion_grilla[1]
    
    etiqueta_variable = tk.Label(contenedor, text="")
    configurar_etiqueta(etiqueta_variable, fila=FILA, columna=COLUMNA, varias_columnas=cantidad_columnas, fuente=(TIPO_TEXTO_DE_FUENTE, 12))

    return etiqueta_variable

def instanciar_botones_interfaz_ingreso(
                                        frame_de_ingreso,
                                        etiqueta_variable,
                                        casilla_nombre_de_usuario,
                                        casilla_contrasenia,
                                        listado_de_jugadores,
                                        cuentas_registradas,
                                        numero_max_jugadores,
                                        raiz_de_ingreso,
                                        boton_externo
                                       ):
    """
    Instancia todos los botones de la interfaz de ingreso y los configura.
    """
    # - Botón 'Ingresar' - #
    boton_ingresar = tk.Button(
                               frame_de_ingreso,
                               text='Ingresar',
                               command=lambda: verificar_ingreso(
                                                                 boton_ingresar,
                                                                 etiqueta_variable,
                                                                 casilla_nombre_de_usuario,
                                                                 casilla_contrasenia,
                                                                 listado_de_jugadores,
                                                                 cuentas_registradas,
                                                                 numero_max_jugadores
                                                                )
                              )
    configurar_boton(boton_ingresar, fila=3, columna=1)

    # - Botón 'Volver' - #
    boton_volver = tk.Button(
                             frame_de_ingreso,
                             text='Volver',
                             command=lambda: destruir_interfaz(
                                                               raiz_de_ingreso,
                                                               boton_externo
                                                              )
                            )
    configurar_boton(boton_volver, fila=3, columna=0)

def verificar_ingreso(
                      boton_ingresar,
                      etiqueta_variable,
                      casilla_nombre,
                      casilla_contrasenia,
                      listado_de_jugadores,
                      cuentas_registradas,
                      numero_max_jugadores
                     ):
    """
    Recibe el ingreso de un jugador, valida que sea correcto.
    En caso de no serlo, notifica que hubo algún error en los datos ingresados.
    En caso de que sean correctos, agrega el registro en la estructura que
    contiene todas las cuentas registradas.
    
    Pre: -boton_ingresar: Corresponde a una instancia de la clase 'Button'
                          (del módulo tkinter).
         -etiqueta_variable: Corresponde a una instancia de la clase 'Label'
                             (del módulo tkinter). 
         -casilla_nombre: Corresponde a una instancia de la clase 'Entry' (del
                          módulo tkinter).
         -casilla_contrasenia: Corresponde a una instancia de la clase 'Entry'
                               (del módulo tkinter).
         -cuentas_registradas: Debe ser un diccionario.
         -listado_de_jugadores: Debe ser una lista.
         -numero_max_jugadores: No debe ser ni una lista, ni una tupla, ni un
                                diccionario.
    """
    nombre = casilla_nombre.get().lower()
    MENSAJE_REINGRESO = f"El usuario '{nombre}' ya se ingresó."
    MENSAJE_EXITO = f"El usuario '{nombre}' ha sido ingresado con éxito."
    
    if (len(listado_de_jugadores) < numero_max_jugadores) and not (nombre in listado_de_jugadores):
        contrasenia = casilla_contrasenia.get()

        if (nombre == "") and (contrasenia != ""):
            etiqueta_variable["text"] = "El campo de usuario es obligatorio"
        elif (nombre != "") and (contrasenia == ""):
            if nombre in cuentas_registradas.keys():
                etiqueta_variable["text"] = MENSAJE_CONTRASENIA_INCORRECTA
            else:
                limpiar_casillas([casilla_nombre, casilla_contrasenia])
                etiqueta_variable["text"] = MENSAJE_ERROR_INGRESO
        elif (nombre != "") and (contrasenia != ""):
            etiqueta_variable["text"] = "Verificando ingreso..."
            if nombre in cuentas_registradas.keys():
                if (contrasenia == cuentas_registradas[nombre]):
                    if nombre in listado_de_jugadores:
                        limpiar_casillas([casilla_nombre, casilla_contrasenia])
                        etiqueta_variable["text"] = MENSAJE_REINGRESO
                    else:
                        limpiar_casillas([casilla_nombre, casilla_contrasenia])
                        etiqueta_variable["text"] = MENSAJE_EXITO
                        listado_de_jugadores.append(nombre)
                else:
                    limpiar_casillas([casilla_contrasenia])
                    etiqueta_variable["text"] = MENSAJE_CONTRASENIA_INCORRECTA
            else:
                limpiar_casillas([casilla_nombre, casilla_contrasenia])
                etiqueta_variable["text"] = MENSAJE_ERROR_INGRESO
    elif nombre in listado_de_jugadores:
        limpiar_casillas([casilla_nombre, casilla_contrasenia])
        etiqueta_variable["text"] = MENSAJE_REINGRESO
    else:
        boton_ingresar["state"] = "disabled"
        etiqueta_variable["text"] = MENSAJE_MAXIMO_INGRESO
        messagebox.showwarning("¡Atención!", MENSAJE_MAXIMO_INGRESO)
        limpiar_casillas([casilla_nombre, casilla_contrasenia])

def limpiar_casillas(casillas):
    """
    Borra el contenido de todas las casillas de texto contenidas en la
    estructura iterable enviada por parámetro.
    Pre: -casillas: Corresponde a una estructura iterable que contiene
                    instancias de la clase 'Entry' (del módulo tkinter).
    """
    for casilla in casillas:
        casilla.delete(0, "end")

def destruir_interfaz(interfaz_a_destruir, boton=None, listado_de_jugadores=[]):
    """
    Destruye una interfaz gráfica y todos los objetos que contiene la misma.
    Si se presiona el botón que contiene el texto 'Salir' o la cruz superior
    derecha de la ventana, se limpia la lista de jugadores.
    Pre: -listado_de_jugadores: Corresponde a una lista.
    """
    es_ventana_cerrada = False
    try:
        if boton:
            boton["state"] = "normal"
            if ((boton["text"] == "Salir") and (len(listado_de_jugadores) != 0)):
                listado_de_jugadores.clear()
            interfaz_a_destruir.destroy()
        else:
            es_ventana_cerrada = messagebox.askyesno(VENTANA_EMERGENTE_SALIR, MENSAJE_CERRAR)
    except tk.TclError:
        interfaz_a_destruir.destroy()

    if es_ventana_cerrada:
        listado_de_jugadores.clear()
        interfaz_a_destruir.destroy()

def ejecutar_interfaz_de_registro(boton_externo, cuentas_registradas):
    """
    Ejecuta la interfaz de registro.
    """
    boton_externo["state"] = "disabled"

    # - Raíz de registro de jugadores - #
    raiz_de_registro = tk.Tk()
    configurar_raiz(raiz_de_registro, titulo="Registro de jugador", icono="usuario.ico")

    # - Frame de registro - #
    frame_de_registro = tk.Frame(raiz_de_registro)
    configurar_frame(frame_de_registro)

    instanciar_etiquetas_interfaz_registro(frame_de_registro)

    # - Campo de texto de nombre de usuario - #
    casilla_nombre_de_usuario = instanciar_campo_de_texto(frame_de_registro, ubicacion_grilla=(1, 1))

    # - Campo de texto de contraseña - #
    casilla_contrasenia = instanciar_campo_de_texto(frame_de_registro, ubicacion_grilla=(3, 1), caracter_a_exhibir="*")

    # - Campo de texto de Repetir contraseña - #
    casilla_repetir_contrasenia = instanciar_campo_de_texto(frame_de_registro, ubicacion_grilla=(5, 1), caracter_a_exhibir="*")
    
    # - Etiqueta identificadora de error al ingresar el nombre de usuario - #
    etiqueta_variable_de_usuario = instanciar_etiqueta_variable(frame_de_registro, ubicacion_grilla=(2, 1))

    # - Etiqueta identificadora de error al ingresar la contraseña - #
    etiqueta_variable_de_contrasenia = instanciar_etiqueta_variable(frame_de_registro, ubicacion_grilla=(4, 1))

    # - Etiqueta identificadora variable - #
    etiqueta_variable = instanciar_etiqueta_variable(frame_de_registro, ubicacion_grilla=(7, 0), cantidad_columnas=2)

    # - Botón de chequeo (para mostrar contraseña) - #
    instanciar_boton_chequeo(frame_de_registro, casilla_contrasenia, ubicacion_grilla=(3, 2))

    # - Botón de chequeo (para mostrar contraseña) - #
    instanciar_boton_chequeo(frame_de_registro, casilla_repetir_contrasenia, ubicacion_grilla=(5, 2))


    instanciar_botones_interfaz_registro(
                                         frame_de_registro,
                                         etiqueta_variable,
                                         etiqueta_variable_de_usuario,
                                         etiqueta_variable_de_contrasenia,
                                         casilla_nombre_de_usuario,
                                         casilla_contrasenia,
                                         casilla_repetir_contrasenia,
                                         cuentas_registradas,
                                         raiz_de_registro,
                                         boton_externo
                                        )

    raiz_de_registro.protocol('WM_DELETE_WINDOW', func=lambda: destruir_interfaz(raiz_de_registro, boton_externo))
    raiz_de_registro.mainloop()

def instanciar_etiquetas_interfaz_registro(frame_de_registro):
    """
    Instancia todas las etiquetas, de la interfaz de registro, que tendrán un
    texto constante y las configura.
    """
    # - Etiqueta 'Registro de usuario' - #
    etiqueta_titulo_registro = tk.Label(frame_de_registro, text="Registro de usuario")
    configurar_etiqueta(etiqueta_titulo_registro, fila=0, columna=0, varias_columnas=2, fuente=(TIPO_TEXTO_DE_FUENTE, 18))
    
    # - Etiqueta 'Nombre de usuario:' - #
    etiqueta_nombre = tk.Label(frame_de_registro, text="Nombre de usuario:")
    configurar_etiqueta(etiqueta_nombre, fila=1, columna=0, orientacion="e")
    
    # - Etiqueta 'Contraseña:' - #
    etiqueta_contrasenia = tk.Label(frame_de_registro, text="Contraseña:")
    configurar_etiqueta(etiqueta_contrasenia, fila=3, columna=0, orientacion="e")
    
    # - Etiqueta 'Repetir Contraseña:' - #
    etiqueta_contrasenia = tk.Label(frame_de_registro, text="Repitir contraseña:")
    configurar_etiqueta(etiqueta_contrasenia, fila=5, columna=0, orientacion="e")

def instanciar_botones_interfaz_registro(
                                         frame_de_registro,
                                         etiqueta_variable,
                                         etiqueta_variable_de_usuario,
                                         etiqueta_variable_de_contrasenia,
                                         casilla_nombre_de_usuario,
                                         casilla_contrasenia,
                                         casilla_repetir_contrasenia,
                                         cuentas_registradas,
                                         raiz_de_registro,
                                         boton_externo
                                        ):
    """
    Instancia todos los botones de la interfaz de registro y los configura.
    """
    # - Botón 'Registrar' - #
    boton_registrar = tk.Button(
                                frame_de_registro,
                                text='Registrar',
                                command=lambda: cargar_registro(
                                                                etiqueta_variable,
                                                                etiqueta_variable_de_usuario,
                                                                etiqueta_variable_de_contrasenia,
                                                                casilla_nombre_de_usuario,
                                                                casilla_contrasenia,
                                                                casilla_repetir_contrasenia,
                                                                cuentas_registradas
                                                                )
                               )
    configurar_boton(boton_registrar, fila=6, columna=1)

    # - Botón 'Volver' - #
    boton_volver = tk.Button(frame_de_registro, text='Volver', command=lambda: destruir_interfaz(raiz_de_registro, boton_externo))
    configurar_boton(boton_volver, fila=6, columna=0)

def cargar_registro(
                    etiqueta_variable,
                    etiqueta_variable_de_usuario,
                    etiqueta_variable_de_contrasenia,
                    casilla_nombre, casilla_contrasenia,
                    casilla_repetir_contrasenia,
                    cuentas_registradas
                   ):
    """
    Valida el ingreso del usuario y la contraseña.
    Si es correcto, verifica que el usuario no esté registrado y lo registra.
    En el caso en que ya se encuentre registrado, notifica por pantalla.
    Si el ingreso es incorrecto, notifica por pantalla.
    """
    nombre = casilla_nombre.get().lower()
    contrasenia = casilla_contrasenia.get()
    contrasenia_repetida = casilla_repetir_contrasenia.get()
    MENSAJE_EXITO_REGISTRO = f"El usuario '{nombre}' ha sido registrado correctamente."
    MENSAJE_NOMBRE_REGISTRADO  = f"El usuario '{nombre}' ya se encuentra registrado."
    MENSAJE_NOMBRE_INVALIDO = "No es un usuario válido."
    MENSAJE_CONTRASENIA_INVALIDA = "No es una contraseña válida."
    MENSAJE_CONTRASENIAS_DESIGUALES = "Las contraseñas no coinciden."

    if es_usuario_valido(nombre) and es_contrasenia_valida(contrasenia) and (contrasenia == contrasenia_repetida):
        if not nombre in cuentas_registradas.keys():
            salvar_registro(nombre, contrasenia)
            cuentas_registradas[nombre] = contrasenia
            etiqueta_variable["text"] = MENSAJE_EXITO_REGISTRO
            limpiar_casillas([casilla_nombre, casilla_contrasenia, casilla_repetir_contrasenia])
            limpiar_etiquetas([etiqueta_variable_de_usuario, etiqueta_variable_de_contrasenia])
        else:
            etiqueta_variable["text"] = MENSAJE_NOMBRE_REGISTRADO
            limpiar_casillas([casilla_nombre, casilla_contrasenia, casilla_repetir_contrasenia])
            limpiar_etiquetas([etiqueta_variable_de_usuario, etiqueta_variable_de_contrasenia])

    elif not es_usuario_valido(nombre):
        etiqueta_variable_de_usuario["text"] = MENSAJE_NOMBRE_INVALIDO
        limpiar_etiquetas([etiqueta_variable_de_contrasenia, etiqueta_variable])

    elif not es_contrasenia_valida(contrasenia):
        etiqueta_variable_de_contrasenia["text"] = MENSAJE_CONTRASENIA_INVALIDA
        limpiar_etiquetas([etiqueta_variable_de_usuario, etiqueta_variable])

    elif (contrasenia != contrasenia_repetida):
        etiqueta_variable["text"] = MENSAJE_CONTRASENIAS_DESIGUALES
        limpiar_etiquetas([etiqueta_variable_de_contrasenia, etiqueta_variable_de_usuario])

def es_usuario_valido(usuario):
    """
    Valida el ingreso del nombre de usuario.
    Pre: -usuario: Debe ser un tipo de dato al que se accede por
                   subindice. 
    Post: Retorna True si el ingreso es válido, o False en caso contrario.
    
    Casos de prueba:
    >>> es_usuario_valido("aaaa")
    True
    >>> es_usuario_valido("Pepa")
    True
    >>> es_usuario_valido("123456789")
    True
    >>> es_usuario_valido("____")
    True
    >>> es_usuario_valido("PepE_123")
    True
    >>> es_usuario_valido("pepe_1234567890")
    True
    >>> es_usuario_valido("P3PÉ_al")
    True
    >>> es_usuario_valido("PepE")
    True
    >>> es_usuario_valido("PEPE,123")
    False
    >>> es_usuario_valido("pepe_12345678908")
    False
    >>> es_usuario_valido("Pep")
    False
    >>> es_usuario_valido("Pepe@34")
    False
    >>> es_usuario_valido("pepe_/")
    False
    """
    GUION_BAJO = "_"
    LARGO_DE_USUARIO = len(usuario)
    es_usuario_correcto = True
    if (CANTIDAD_MIN_CARACTERES_USUARIO <= LARGO_DE_USUARIO <= CANTIDAD_MAX_CARACTERES_USUARIO):
        indice = 0
        while (indice < LARGO_DE_USUARIO) and es_usuario_correcto:
            caracter = usuario[indice]
            if not caracter.isalnum() and (caracter != GUION_BAJO):
                es_usuario_correcto = False
            indice += 1
    else:
        es_usuario_correcto = False

    return es_usuario_correcto

def es_contrasenia_valida(contrasenia):
    """
    Valida el ingreso de la contraseña.
    Pre: -contrasenia: Debe ser un tipo de dato al que se accede por
                       subindice. 
    Post: Retorna True si la contraseña es válida, False en caso contrario.
    Casos de prueba:
    >>> es_contrasenia_valida("GoLazOde-ma7")
    True
    >>> es_contrasenia_valida("GoLazO_dema7")
    True
    >>> es_contrasenia_valida("Golazodema7-")
    True
    >>> es_contrasenia_valida("Golazodema7_")
    True
    >>> es_contrasenia_valida("Golazo7_")
    True
    >>> es_contrasenia_valida("GoLazO-de-ma")
    False
    >>> es_contrasenia_valida("GoLazOdema7")
    False
    >>> es_contrasenia_valida("golazodema7_")
    False
    >>> es_contrasenia_valida("golazodema7-")
    False
    >>> es_contrasenia_valida("pepe_/")
    False
    >>> es_contrasenia_valida("GoLazO-demá7")
    False
    >>> es_contrasenia_valida("Golazo_de7maradonA")
    False
    """
    GUION_VALIDO = "_-"
    LARGO_DE_CONTRASENIA = len(contrasenia)
    es_contrasenia_correcta = True
    hay_mayuscula = False
    hay_minuscula = False
    hay_numero = False
    hay_guion = False
    if (CANTIDAD_MIN_CARACTERES_CONTRASENIA <= LARGO_DE_CONTRASENIA <= CANTIDAD_MAX_CARACTERES_CONTRASENIA):
        indice = 0
        while (indice < LARGO_DE_CONTRASENIA) and es_contrasenia_correcta:
            caracter = contrasenia[indice]
            if caracter.lower() in LETRAS_ACENTUADAS:
               es_contrasenia_correcta = False
            elif caracter.isupper():
                hay_mayuscula = True
            elif caracter.islower():
                hay_minuscula = True
            elif caracter.isdigit():
                hay_numero = True
            elif caracter in GUION_VALIDO:
                hay_guion = True
            indice += 1
        if es_contrasenia_correcta and not hay_mayuscula or not hay_minuscula or not hay_numero or not hay_guion:
            es_contrasenia_correcta = False
    else:
        es_contrasenia_correcta = False

    return es_contrasenia_correcta

def salvar_registro(nombre, contrasenia):
    """
    Abre un archivo en modo añadidura.
    Agrega en él el usuario y la contraseña previamente validadas.
    Post: Agrega al final del archivo los datos recibidos.
    """
    with open(REGISTROS_DE_CUENTAS, "a", encoding=CODIFICACION) as archivo:
        archivo.write(f"{nombre},{contrasenia}\n")

def limpiar_etiquetas(etiquetas):
    """
    Borra el contenido de una etiqueta.
    Pre: -etiquetas: Es un tipo de dato iterable que contiene instancias de
                     una clase del módulo tkinter.
    """
    for etiqueta in etiquetas:
        etiqueta["text"] = ""

def ejecutar_interfaz_principal(numero_max_jugadores):
    """
    Ejecuta todas las interfaces.
    
    Post: En caso de iniciar la partida, devuelve una lista con los usuarios ingresados.
          En caso de salir o cerrar la interfaz, devuelve una lista vacía.
    """
    print(doctest.testmod())
    
    print("Ejecutando interfaz ...\n")
    listado_de_jugadores = []
    cuentas_registradas = traer_registro_de_cuentas()

    # - Raíz - #
    raiz = tk.Tk()
    raiz.attributes('-topmost', True)
    raiz.after_idle(raiz.attributes,'-topmost', False)

    configurar_raiz(
                    raiz,
                    titulo="Menú de opciones",
                    dimensionable="ambos",
                    icono="icono_ahorcado_2.ico"
                   )

    # - Imágenes (del grupo revelación y del juego) - #
    imagen_revelacion = tk.PhotoImage(file=IMAGEN_GRUPO)
    imagen_ahorcado = tk.PhotoImage(file=IMAGEN_JUEGO)

    instanciar_etiquetas_de_imagen_interfaz_principal(raiz, imagen_revelacion, imagen_ahorcado)

    # - Frame de opciones - #
    frame_de_opciones = tk.Frame(raiz)
    configurar_frame(frame_de_opciones, ubicacion_grilla=(1, 1))

    instanciar_etiquetas_interfaz_principal(frame_de_opciones)

    instanciar_botones_interfaz_principal(
                                 frame_de_opciones,
                                 listado_de_jugadores,
                                 numero_max_jugadores,
                                 cuentas_registradas,
                                 raiz
                                )

    raiz.protocol('WM_DELETE_WINDOW',
                   func=lambda: destruir_interfaz(
                                                  raiz,
                                                  listado_de_jugadores=listado_de_jugadores
                                                 )
                 )
    
    raiz.mainloop()
    print("Interfaz finalizada con éxito.\n")
    return listado_de_jugadores
