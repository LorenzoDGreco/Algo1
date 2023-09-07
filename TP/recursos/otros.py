
# - CON ESTO PRUEBO COMO SE HACE EL DOCTEST DE UNA FUNCION CON INPUT() (todavia no funciona) - #
# def pedir_cadena():
#     """
#     Casos de prueba:
#     >>> pedir_cadena()
#     Ingresa algo: 'hola'
#     'hola'
#     >>> pedir_cadena()
#     Ingresa algo: 'chau'
#     'chau'
#     >>> pedir_cadena()
#     Ingresa algo: 'Algoritmos y programacion'
#     'Algoritmos y programacion'
#     >>> pedir_cadena()
#     Ingresa algo: 'Filosofia y letras'
#     'Filosofia y letras'
#     >>> pedir_cadena()
#     Ingresa algo: 'musica y danza'
#     'musica y danza'
#     >>> pedir_cadena()
#     Ingresa algo: 'UBA'
#     'UBA'
#     """
#     cadena = input("Ingresa algo: ")
#     return cadena

# Ejemplo de modularizacion.
"""def instanciar_botones(ventana_de_anclaje): # VER DE MODIFICAR O SACAR

    Instancia todos los botones de la ventana en la que se ubicarán.

    # - Botón 'Ingresar' - #
    boton_ingresar = instanciar_boton(ventana_de_anclaje, 'Ingresar', ejecutar_interfaz_de_ingreso(boton_ingresar))
    configurar_boton(boton_ingresar, fila = 2, columna = 0)

    # - Botón 'Registrar' - #
    boton_registrar = instanciar_boton(ventana_de_anclaje, 'Registrar', ejecutar_interfaz_de_registro(boton_registrar, cuentas_registradas))
    configurar_boton(boton_registrar, fila = 3, columna = 0)

    # - Botón 'Iniciar partida' - #
    boton_iniciar = tk.Button(ventana_de_anclaje, text = 'Iniciar partida', width = ANCHO_BOTON, command = "")
    boton_iniciar = instanciar_boton(ventana_de_anclaje, 'Iniciar partida', instruccion = "")
    configurar_boton(boton_iniciar, fila = 4, columna = 0)

    # - Botón 'Cancelar' - #
    # command=lambda: [fun1(), fun2()]
    boton_cancelar = instanciar_boton(ventana_de_anclaje, 'Cancelar', destruir_interfaz(raiz, boton_cancelar))
    configurar_boton(boton_cancelar, fila = 5, columna = 0, identificador_boton = "boton cancelar")

def instanciar_boton(ventana_de_anclaje, nombre_de_boton, instruccion): # VER DE MODIFICAR O SACAR
    """
"""return tk.Button(ventana_de_anclaje, text = nombre_de_boton, width = ANCHO_BOTON, command = instruccion)"""
