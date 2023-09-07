# ------------------------ Importación de librerías ------------------------ #
# Python
import pathlib
import random
import doctest

# Internas
from constantes_de_texto import (
                                 SALUDO_INICIAL,
                                 CADENAS_DE_FIN,
                                 CARACTER_CENSURA,
                                 LETRAS_CORRECTAS,
                                 LETRAS_Y_CARACTERES_ESPECIALES,
                                 NO,
                                 SI,
                                 LARGO_ALEATORIO,
                                 RUTA_TEXTOS,
                                 FIN,
                                 MAX_USUARIOS,
                                 LARGO_MINIMO,
                                 MAXIMOS_DESACIERTOS,
                                 PUNTOS_POR_DESACIERTO,
                                 PUNTOS_POR_ACIERTO,
                                 PUNTOS_ADIVINA_PALABRA,
                                 PUNTOS_RESTA_GANA_PROGRAMA,
                                 CODIFICACION
                                )

from constantes_enteras import (
                                PRIMER_PARTIDA,
                                RESTO_DE_PARTIDAS,
                                MINIMO_DE_CARACTER_CENSURA,
                                LETRA_MAX,
                                PALABRA,
                                CANT_TOT,
                                PUNTOS,
                                DESACIERTOS,
                                ACIERTOS,
                                CANTIDAD_PARTIDAS_GANADAS
                               )

from interfaz_grafica import ejecutar_interfaz_principal

# -------------------- Definición de funciones propias --------------------- #

def formar_diccionario_config(diccionario_config, contador_partidas):
    """
    Pregunta al usuario si desea cambiar la configuracion del juego. En caso
    de que el jugador quiera cambiar la configuracion, se le preguntan los nuevos
    valores y se almacenan en el diccionario ya formado con la configuracion
    inicial. Devuelve el diccionario de configuracion.

    Post: Retorna el diccionario configuraciones iniciales o cambiadas según lo que
            el usuario desee
    """
    if (contador_partidas >= RESTO_DE_PARTIDAS):
        print("Considere que si desea cambiar la configuración maxima de jugadores del juego se reiniciarán los datos de la partida.")

    cambiar_config = input("Quiere cambiar la configuracion del juego? (s/n) ").lower()

    while cambiar_config != SI and cambiar_config != NO:
            cambiar_config = input("Error. Ingrese lo mencionado (s/n): ")

    if not diccionario_config:
        diccionario_config = mantener_config_inicial()

    if cambiar_config == SI:
        nueva_config(diccionario_config)

    print("La configuración del juego ha finalizado con éxito!\n")
    return diccionario_config

def mantener_config_inicial():
    """
    Genera el diccionario con los valores de configuracion
    predeterminados. Devuelve dicho diccionario.

    Pre: tiene que existir la carpeta textos, sub carpeta texto_configuracion y
     su archivo configuracion.csv
    Post: Devuelve el diccionario con los valores por defecto
    """
    diccionario_config = {}
    archivo = open("textos\\texto_configuracion\\configuracion.csv", "r", encoding=CODIFICACION)
    linea = leer_linea(archivo)
    aspecto_config, valor = linea.rstrip("\n").split(",")

    while aspecto_config != FIN:
        diccionario_config[aspecto_config] = int(valor)
        linea = leer_linea(archivo)
        if linea != FIN:
            aspecto_config, valor = linea.rstrip("\n").split(",")
        else:
            aspecto_config = FIN

    archivo.close()

    return diccionario_config

def leer_linea(archivo):
    """
    Lee una linea del archivo.

    Pre: Debe de llegar un archivo de lectura
    """
    linea = archivo.readline()
    return linea if linea else FIN

def nueva_config(diccionario_config):
    """
    Muestra los valores actuales de configuracion y pide al usuario que
    ingrese los valores nuevos, que reemplazaran a los valores ya
    existentes. Devuelve el diccionario con los valores nuevos.

    Pre: Debe de llegarle un diccionario no vacio
    Post: Devuelve un nuevo diccionario con las configuraciones del usuario
    """
    for configuracion, valor in diccionario_config.items():
        print("\nLa configuracion ",configuracion,
                "es actualmente: ",valor,
                " ingrese un nuevo valor: ", end = "")

        valor = input()
        while valor.isalpha() or not valor.isalnum():
            valor = input("Error. Ingrese un valor numerico y positivo: ")
        diccionario_config[configuracion] = int(valor)
    return diccionario_config

def generar_jugadores(listado_jugadores):
    """
    Genera un diccionario que almacena todos los jugadores
    con sus respectivos datos del juego.

    Pre: Recibe un listado de jugadores no vacio
    Post: Retorna un diccionario {Usuario:{Config:Valor}}
    """
    PARTIDA = {
        "letra_a_verificar": "",
        "letras_ingresadas": [],
        "letras_erroneas": [],
        "puntos": 0,
        "desaciertos": 0,
        "aciertos": 0,
        "palabra_a_descubrir": "",
        "palabra_censurada": "",
    }
    datos_jugador = {}
    for jugador in listado_jugadores:
        datos_jugador[jugador] = PARTIDA.copy()

    return datos_jugador

def seguir_jugando(contador_partidas):
    """
    Obliga al usuario ingresar bien el chequeo para que sea s/n

    Post: Al ingresar los caracteres validos los retorna.
    """
    MENSAJE = "Desea jugar otra partida? (S/N): "
    chequeo = SI
    if (contador_partidas >= RESTO_DE_PARTIDAS):
        chequeo = input(MENSAJE).lower().strip()
        while not (chequeo in (SI, NO)):
            chequeo = input("Realiza un ingreso valido (S/N): ").lower().strip()

    return (chequeo == SI)

def leer_archivos(diccionario_config):
    """
    Lee los multiples n° archivos ingresados en la carpeta textos y los guarda en un diccionario

    Pre: Debe existir la carpeta texto con al menos un texto para la lectura
    Post: Genera y retorna un diccionario de palabras compuesto por los n° textos
    """
    diccionario_palabras = {}
    nombre_archivos = leer_nombre_archivos()
    archivos = [0 for x in range(len(nombre_archivos))]

    for i in range(len(nombre_archivos)):

        archivos[i] = open("textos\\" + nombre_archivos[i], "r", encoding=CODIFICACION)
        linea = leer_linea(archivos[i])

        while (linea != FIN):
            diccionario_palabras = extraer_palabras(
                linea, diccionario_palabras, nombre_archivos, i, diccionario_config)

            linea = leer_linea(archivos[i])

        archivos[i].close()

    return diccionario_palabras

def leer_nombre_archivos():
    """
    Lee los nombres de los archivos en la ruta "\\textos\\" ignorando las carpetas

    Pre: Debe existir la carpeta textos
    Post: Devuelve un diccionario con todos los nombres de los archivos
    """
    directorio = pathlib.Path(RUTA_TEXTOS)
    ficheros = [fichero.name for fichero in directorio.iterdir() if fichero.is_file()]
    return ficheros

def extraer_palabras(linea, diccionario_palabras, nombre_archivos, indice_archivo, diccionario_config):
    """
    Genera un diccionario con todas las palabras posibles del texto
    (que tienen tantos caracteres como indica el largo mínimo elegido).

    Post: Genera diccionario clave: palabra y valor: las veces que se
           repite, por ultimo lo retorna.
    """
    linea = linea.rstrip("\n")
    lista_repeticion = [0 for x in range(len(nombre_archivos))]
    palabra = ""

    for caracter in linea:
        if caracter.isalpha():
            caracter = aplanar_caracteres(caracter)
            palabra += caracter
        elif (len(palabra) >= int(diccionario_config[LARGO_MINIMO])):
            if not palabra in diccionario_palabras.keys():
                lista_repeticion[indice_archivo] += 1
                diccionario_palabras[palabra] = lista_repeticion
            else:
                lista_repeticion = diccionario_palabras[palabra]
                lista_repeticion[indice_archivo] += 1
                diccionario_palabras[palabra] = lista_repeticion

            palabra = ""
            lista_repeticion = [0 for x in range(len(nombre_archivos))]
        else:
            palabra = ""
    return diccionario_palabras

def aplanar_caracteres(letra):
    """
    Recibe una letra y le sobreescribe la letra sin ningún
    caracter especial, si es que tiene

    Pre: Tiene que recibir una unica letra
    Post: Sobreescribe la letra sin caracter especial y la retorna

    >>> aplanar_caracteres("á")
    'a'
    >>> aplanar_caracteres("b")
    'b'
    """
    if not (letra == " ") and not (letra in LETRAS_CORRECTAS):
        for letra_correcta, caracter_especial in LETRAS_Y_CARACTERES_ESPECIALES.items():
            if (letra in caracter_especial):
                letra = letra_correcta
    letra = letra.lower()
    return letra

def crear_lista_ordenada(diccionario_palabras):
    """
    Ordena las palabras por orden alfabético

    Post: Retorna una lista ordenada alfabeticamente

    >>> crear_lista_ordenada({"casa":[1,2,3],"auto":[3,4,1]})
    [('auto', [3, 4, 1]), ('casa', [1, 2, 3])]
    """
    lista_palabras = diccionario_palabras.items()
    lista_palabras = sorted(lista_palabras, key = lambda item : item[0])
    return lista_palabras

def encontrar_largo_max(lista_palabras):
    """
    Busco el largo máximo de todas las palabras

    Post: Retorna el len más largo de toda la lista
    >>> encontrar_largo_max([["alfabeto", [1 ,2 ,3 ]],["casa", [1 ,4 , 5]]])
    8
    """
    largo_palabra_max = 0
    for elementos in lista_palabras:
        if len(elementos[PALABRA]) > largo_palabra_max:
            largo_palabra_max = len(elementos[PALABRA])
    return largo_palabra_max

def escribir_archivo(lista_palabras):
    """
    Escribe todas las palabras en un csv

    Pre: Debe existir la carpeta textos y la sub carpeta texto_resultante
    Post: Crea y/o guarda un nuevo csv
    """
    archivo_palabras = open("textos\\texto_resultante\\archivos_palabras.csv", "w", encoding=CODIFICACION)
    for elemento in lista_palabras:
        cant_archivos = len(lista_palabras[CANT_TOT]) + 1
        archivo_palabras.write(f"{elemento[PALABRA]}")

        for i in range(cant_archivos):
            archivo_palabras.write(f", {elemento[CANT_TOT][i]}")
        archivo_palabras.write("\n")

    archivo_palabras.close()

def indicar_largo_palabra(diccionario_config, largo_palabra_max):
    """
    Solicita el ingreso del largo de una palabra a adivinar.
    Chequea:
        - Si el ingreso está en lo caracteres aleatorios.
        - Si tiene el largo correcto.
        - Si es efectivamente un número.

    Pre: La palabra más larga del texto, contiene 16 caracteres.
    Post: Retorna un largo de palabra.
    """
    es_ingreso_valido = False
    texto= 'Ingrese un largo de la palabra (Enter o "0" para cualquier largo o ingrese entre '\
             + str(diccionario_config[LARGO_MINIMO]) + ' a ' + str(largo_palabra_max) + ' ): '
    largo_palabra = input(texto)

    while not es_ingreso_valido:
        if (largo_palabra in LARGO_ALEATORIO):
            largo_palabra = 0
            es_ingreso_valido = True
        elif largo_palabra.isdigit():
            largo_palabra = int(largo_palabra)
            if (int(diccionario_config[LARGO_MINIMO]) <= int(largo_palabra) <= int(largo_palabra_max)):
                es_ingreso_valido = True

        if not es_ingreso_valido:
            largo_palabra = input('Por favor, ingrese un largo válido de la palabra (Enter o "0" para cualquier largo): ')

    return largo_palabra

def generar_lista(diccionario_palabras, largo_palabra, diccionario_config, largo_palabra_max):
    """
    Genera una nueva lista con el largo total de la palabra ingresada
    por el usuario

    Pre: Recibe un diccionario que contiene como claves palabras y como
         valores un valor entero. y un número que es largo de una palabra.
    Post: Devuelve una lista de palabras candidatas con dicho largo.
    >>> generar_lista({"cazar": 5, "casas": 1}, 5, {"LARGO_MINIMO":5}, 18)
    ['casas', 'cazar']
    >>> generar_lista({"hola":1 ,"cazar": 5, "casas": 1}, 4, {"LARGO_MINIMO":4}, 18)
    ['hola']
    """
    lista_ordenada = sorted(diccionario_palabras.keys())
    lista_palabras_candidatas = []
    if largo_palabra == 0:
        largo_palabra = random.randrange(diccionario_config[LARGO_MINIMO],largo_palabra_max)

    for palabra in lista_ordenada:
        if (len(palabra) == largo_palabra):
            lista_palabras_candidatas.append(palabra)

    return lista_palabras_candidatas

def ordenamiento_partida(diccionario_ganador, contador_partidas):
    """
    Ordena de forma aleatoria los turnos de los jugadores.
    Si la partida que se esta por iniciar, no es la inicial, entonces
    se toma al ganador de la ultima partida como primer jugador, y el
    resto se ordenan de forma aleatoria.
    Pre: el diccionario debe tener como clave un jugador, y como valor True o False.
        el contador de partidas debe ser un entero.
    Post: devuelve la lista con los turnos de los jugadores ya organizados de forma
        aleatoria.
    """
    lista_jugadores = list(diccionario_ganador.keys())
    lista_es_ganador = list(diccionario_ganador.values())
    lista_ganador = []
    turnos_jugadores = []

    if (contador_partidas == PRIMER_PARTIDA):
        random.shuffle(lista_jugadores)
        turnos_jugadores = lista_jugadores
    else:
        posicion_de_estado = 0
        estado = False

        while posicion_de_estado < (len(lista_es_ganador)) and not(estado):
            if lista_es_ganador[posicion_de_estado] == True:
                lista_ganador.append(lista_jugadores.pop(posicion_de_estado))
                estado = True
            posicion_de_estado += 1
        random.shuffle(lista_jugadores)
        turnos_jugadores = lista_ganador + lista_jugadores

    print("\nLos turnos de los jugadores son los siguientes: ", end = "")
    for jugador in turnos_jugadores:
        print(f"-> {jugador} ", end = "")
    print("\n")

    return turnos_jugadores

def definir_palabras_jugadores(datos_jugador, turnos_jugadores, lista_palabras_candidatas):
    """
    Se le asignan a cada jugador en el diccionario (datos_jugador) una palabra con el largo
    pedido por el usuario. Si la cantidad de palabras con ese largo no alcanza para todos los
    usuarios, la funcion permite que se entreguen palabras iguales para 2 o mas jugadores.
    """
    if (len(lista_palabras_candidatas) > len(datos_jugador)):
        lista_palabras_random = []
        i = 0
        
        while (i <= len(datos_jugador)-1):
            palabra_random = random.choice(lista_palabras_candidatas)

            if not palabra_random in lista_palabras_random:
                lista_palabras_random.append(palabra_random)
                datos_jugador[turnos_jugadores[i]]["palabra_a_descubrir"] = palabra_random
                datos_jugador[turnos_jugadores[i]]["palabra_censurada"] = censurar_palabra(datos_jugador[turnos_jugadores[i]]["palabra_a_descubrir"])
                i += 1
    else:
        for i in range(len(datos_jugador)):
            datos_jugador[turnos_jugadores[i]]["palabra_a_descubrir"] = random.choice(lista_palabras_candidatas)
            datos_jugador[turnos_jugadores[i]]["palabra_censurada"] = censurar_palabra(datos_jugador[turnos_jugadores[i]]["palabra_a_descubrir"])

    return datos_jugador

def censurar_palabra(palabra_a_descubrir):
    """
    Censura la palabra enviada por parámetro cambiando todos los caracteres
    por el caracter "?".

    Pre: Recibe una cadena de caracteres que representa la palabra a adivinar.
    Post: Retorna una cadena de caracteres con los cambios mencionados.
    >>> censurar_palabra("casa")
    '????'
    >>> censurar_palabra("australopithecus")
    '????????????????'
    >>> censurar_palabra("supercalifragilisticoespialidoso")
    '????????????????????????????????'
    """
    palabra_censurada = ""
    for _ in range(len(palabra_a_descubrir)):
        palabra_censurada += CARACTER_CENSURA
    return palabra_censurada

def mostrar_estado(datos_jugador, turno):
    """
    Muestra por pantalla el estado de la partida. Esto incluye: El estado de la
    palabra censurada, la cantidad de aciertos, desaciertos y las letras
    erróneas.

    Pre: Recibe una cadena de caracteres que representa la palabra a adivinar
         (que puede contener "?" y letras desbloqueadas simultáneamente), la
         cantidad de aciertos (int), la cantidad de desaciertos (int) y una
         lista que contiene todas las letras erróneas ingresadas.
    Post: Imprime por pantalla el estado mencionado.
    """
    palabra_censurada = datos_jugador["palabra_censurada"]
    aciertos = datos_jugador["aciertos"]
    desaciertos = datos_jugador["desaciertos"]
    letras_erroneas = datos_jugador["letras_erroneas"]
    print(f"Jugador: {turno}, Palabra a adivinar: {palabra_censurada}, Aciertos: {aciertos}, Desaciertos: {desaciertos}", end = "")
    if desaciertos:
        for elementos in letras_erroneas:
            print(f" - {elementos}", end="")
    print("\n")

def ingresar_letra(datos_jugador):
    """
    Pide el ingreso de una letra hasta que esta sea válida. Cuando esto ocurra,
    retorna la letra ingresada. Si la letra ingresada es la cadena FIN o el cero,
    devuevle esos caracteres. Si ha ingresado la palabra completa que es correcta la retorna,
    o si el largo de la palabra completa es la misma pero no sean iguales la retorna.

    Pre: Recibe una lista que contiene todas las letras ingresadas hasta el
         momento (tanto las acertadas como las erróneas).
    Post: Retorna la letra ingresada en caso de ser válida o ser FIN/0.
    """
    letras_ingresadas = datos_jugador["letras_ingresadas"]
    palabra_a_descubrir = datos_jugador["palabra_a_descubrir"]
    letra_a_verificar = input("-> Ingrese letra: ").lower().strip()

    if (len(letra_a_verificar) <= LETRA_MAX):
        letra_a_verificar = aplanar_caracteres(letra_a_verificar)
    else:
        letra_a_verificar = aplanar_palabra_completa(letra_a_verificar)

    while es_letra_valida(letra_a_verificar, palabra_a_descubrir, letras_ingresadas):

        if (letra_a_verificar in letras_ingresadas):
            print("Letra ya ingresada")
        else:
            print("Ingreso invalido.")
        letra_a_verificar = input("Ingrese nuevamente una letra: ").lower().strip()

    return letra_a_verificar

def aplanar_palabra_completa(letra_a_verificar):
    """
    Se encarga de quitar todos los caracteres especiales de la palabra completa

    Pre:  Tiene que recibir un string no vacío
    Post: Retorna un nuevo string formado del anterior cambiando caracteres
           especiales por normales
    >>> aplanar_palabra_completa("á")
    'a'
    >>> aplanar_palabra_completa("Ø")
    'o'
    >>> aplanar_palabra_completa("a")
    'a'
    """
    palabra_aplanada = ""
    sin_intercambios = False
    for caracter in letra_a_verificar:
        for letra_correcta, caracter_especial in LETRAS_Y_CARACTERES_ESPECIALES.items():
            if (caracter in caracter_especial):
                palabra_aplanada += letra_correcta
                sin_intercambios = True
        if (not sin_intercambios):
            palabra_aplanada += caracter
        sin_intercambios = False
    return palabra_aplanada

def es_letra_valida(letra_a_verificar, palabra_a_descubrir, letras_ingresadas):
    """
    Recibe una letra, una palabra y una lista con las letras ingresadas.
    Devuelve si es válida.

    Pre: Recibe letra a verificar, una palabra censurada y una lista de letras ingresadas.
    Post: Retorna un booleano dependiendo si la letra es valida.
    >>> es_letra_valida("0", "casa", ['w', 't', 'q', 'r'])
    False
    >>> es_letra_valida("@", "casa", ['w', 't', 'q', 'r'])
    True
    """
    return (not letra_a_verificar == palabra_a_descubrir \
            and not (letra_a_verificar in CADENAS_DE_FIN))\
            and (not ((len(letra_a_verificar) == LETRA_MAX) or (len(letra_a_verificar) == len(palabra_a_descubrir)))
            or not letra_a_verificar.isalpha() \
            or letra_a_verificar in letras_ingresadas)

def almacenar_letras_ingresadas(datos_jugador):
    """
    Agrega la letra ingresada a la lista que contiene todas letras ingresadas
    (tanto las acertadas como las desacertadas).

    Pre: Recibe una letra ingresada por el usuario (previamente validada)
         y la lista que contiene todas las letras ingresadas.
    Post: Devuelve la lista que contiene las letras ingresadas con los cambios
          mencionados.
    >>> almacenar_letras_ingresadas({"letra_a_verificar":"w", "letras_ingresadas":['q', 's', 'f', 'g']})
    ['q', 's', 'f', 'g', 'w']
    >>> almacenar_letras_ingresadas({"letra_a_verificar":"q", "letras_ingresadas":['q', 's', 'f', 'g']})
    ['q', 's', 'f', 'g']
    """
    letra = datos_jugador["letra_a_verificar"]
    letras_ingresadas = datos_jugador["letras_ingresadas"]
    return letras_ingresadas + [letra] if ((not letra in letras_ingresadas) and letra.isalpha()) else letras_ingresadas

def contar_aciertos(datos_jugador):
    """
    Cuenta la cantidad de letras correctas/acertadas que ingreso el usuario
    hasta el momento.

    Pre: Recibe la letra (previamente validada en su ingreso) a verificar, la
         palabra a descubrir en su estado actual, el acumulador de la cantidad
         de aciertos hasta el momento.
    Post: Devuelve el acumulador de la cantidad de aciertos (int).
    >>> contar_aciertos({"letra_a_verificar":"w", "palabra_a_descubrir":"casa", "aciertos":0})  
    0
    >>> contar_aciertos({"letra_a_verificar":"a", "palabra_a_descubrir":"casa", "aciertos":0})
    Muy bien!!!
    1
    """
    letra_a_verificar = datos_jugador["letra_a_verificar"]
    palabra_a_descubrir = datos_jugador["palabra_a_descubrir"]
    aciertos = datos_jugador["aciertos"]
    if (letra_a_verificar in palabra_a_descubrir):
        aciertos += 1
        print("Muy bien!!!")
    return aciertos

def contar_desaciertos(datos_jugador):
    """
    Cuenta la cantidad de letras fallidas/desacertadas que ingreso el usuario
    hasta el momento.

    Pre: Recibe la letra (previamente validada en su ingreso) a verificar, un
          string no nulo.
    Post: Devuelve el acumulador de la cantidad de desaciertos (int) y los puntos
           restados (int)
    >>> contar_desaciertos({"letra_a_verificar":"w", "palabra_a_descubrir":"casa", "desaciertos":1})
    <BLANKLINE>
    Lo siento!!!
    2
    >>> contar_desaciertos({"letra_a_verificar":"a", "palabra_a_descubrir":"casa", "desaciertos":0})
    0
    """
    letra_a_verificar = datos_jugador["letra_a_verificar"]
    palabra_a_descubrir = datos_jugador["palabra_a_descubrir"]
    desaciertos = datos_jugador["desaciertos"]
    if not (letra_a_verificar in palabra_a_descubrir) and not (letra_a_verificar in CADENAS_DE_FIN):
        desaciertos += 1
        print("\nLo siento!!!")
    return desaciertos

def almacenar_letras_erroneas(datos_jugador):
    """
    Verifica si la letra ingresada es errónea y, en caso de serlo, la agrega a
    la lista que contiene las letras erróneas. En caso contrario, no realiza
    ningún cambio sobre la lista.

    Pre: Recibe una letra letra ingresada por el usuario (previamente validada)
         y la lista que contiene las letras erróneas.
    Post: Devuelve la lista que contiene las letras erróneas con los cambios
          mencionados.
    >>> almacenar_letras_erroneas({"letra_a_verificar":"w", "palabra_a_descubrir":"casa", "letras_erroneas":['q', 'r', 't', 'z']})
    ['q', 'r', 't', 'z', 'w']
    >>> almacenar_letras_erroneas({"letra_a_verificar":"a", "palabra_a_descubrir":"casa", "letras_erroneas":['q', 'r', 't', 'z']})
    ['q', 'r', 't', 'z']
    """
    letra_a_verificar  = datos_jugador["letra_a_verificar"]
    palabra_a_descubrir = datos_jugador["palabra_a_descubrir"]
    letras_erroneas = datos_jugador["letras_erroneas"]
    return letras_erroneas + [letra_a_verificar] if not (letra_a_verificar in palabra_a_descubrir) else letras_erroneas

def desbloquear_letra(datos_jugador):
    """
    Reemplaza el caracter ingresado en caso de que este en la palabra a descubrir.

    Pre: Recibe la letra (previamente validada) a verificar y la palabra a
         adivinar en su estado actual.
    Post: Devuelve la palabra censurada con las posiciones de la letra.
    >>> desbloquear_letra({"palabra_a_descubrir":"casa", "palabra_censurada":"c?s?", "letra_a_verificar":"a"})
    'casa'
    >>> desbloquear_letra({"palabra_a_descubrir":"casa", "palabra_censurada":"????", "letra_a_verificar":"c"})
    'c???'
    >>> desbloquear_letra({"palabra_a_descubrir":"casa", "palabra_censurada":"????", "letra_a_verificar":"o"})
    '????'
    """
    letra_a_verificar = datos_jugador["letra_a_verificar"]
    palabra_a_descubrir= datos_jugador["palabra_a_descubrir"]
    palabra_censurada= datos_jugador["palabra_censurada"]
    palabra_a_devolver = ""
    for i in range(len(palabra_a_descubrir)):
        if (palabra_censurada[i] == CARACTER_CENSURA):
            if (letra_a_verificar == palabra_a_descubrir[i]):
                palabra_a_devolver += palabra_a_descubrir[i]
            else:
                palabra_a_devolver += CARACTER_CENSURA
        else:
            palabra_a_devolver += palabra_censurada[i]
    return palabra_a_devolver

def calcular_puntaje(datos_jugador, desaciertos_anterior, palabra_censurada_anterior, diccionario_config):
    """
    Calcula el puntaje total. Si fue un acierto suma 10 puntos por letra adivinada, si fue un
    desacierto resta 5 puntos

    PRE: Recibe desaciertos, desaciertos_anteriores >= 0 y palabra_censurada, palabra_censurada_anterior
          recibe strings no vacios.
    POST: Retornará el valor de los puntos actualizados dependiendo si acertó o no la letra el usuario.
    >>> calcular_puntaje({"letra_a_verificar":"a", "palabra_censurada":"ca?a", "palabra_a_descubrir":"casa", "desaciertos":0}, 0, "c???", {"PUNTOS_ACIERTOS":10})                       
    20
    >>> calcular_puntaje({"letra_a_verificar":"o", "palabra_censurada":"c???", "palabra_a_descubrir":"casa", "desaciertos":1}, 0, "c???", {"PUNTOS_DESACIERTOS":5})  
    -5
    >>> calcular_puntaje({"letra_a_verificar":"casa", "palabra_censurada":"c???", "palabra_a_descubrir":"casa", "desaciertos":0}, 0, "c???", {"PUNTOS_ACIERTOS":10})
    30
    """
    desaciertos = datos_jugador["desaciertos"]
    palabra_censurada= datos_jugador["palabra_censurada"]
    letra_a_verificar = datos_jugador["letra_a_verificar"]
    palabra_a_descubrir = datos_jugador["palabra_a_descubrir"]

    puntos = 0
    if not letra_a_verificar in CADENAS_DE_FIN and (len(letra_a_verificar) == 1):
        if (desaciertos > desaciertos_anterior):
            puntos -= diccionario_config[PUNTOS_POR_DESACIERTO]

        elif (palabra_censurada.count(CARACTER_CENSURA) != -1) and \
                (palabra_censurada.count(CARACTER_CENSURA) < palabra_censurada_anterior.count(CARACTER_CENSURA)):
            restantes_censuradas = (palabra_censurada_anterior.count(CARACTER_CENSURA) - palabra_censurada.count(CARACTER_CENSURA))
            puntos = diccionario_config[PUNTOS_POR_ACIERTO] * restantes_censuradas


    elif not letra_a_verificar in CADENAS_DE_FIN and (letra_a_verificar == palabra_a_descubrir):
        puntos = contar_puntos_por_palabra_completa(datos_jugador, diccionario_config)

    return puntos

def contar_puntos_por_palabra_completa(datos_jugador, diccionario_config):
    """
    Calcula los puntos al ingresar la palabra completa y suma 10 puntos
    por caracter bloqueado "?"

    Pre: Recibe un string no vacío
    Post: Retorna el total de los puntos calculados.
    >>> contar_puntos_por_palabra_completa({"palabra_censurada":"ca?a"}, {"PUNTOS_ACIERTOS":10})
    10
    >>> contar_puntos_por_palabra_completa({"palabra_censurada":"c?s?"}, {"PUNTOS_ACIERTOS":10})
    20
    """
    palabra_censurada = datos_jugador["palabra_censurada"]
    if (len(palabra_censurada) != 1):
        if (palabra_censurada.count(CARACTER_CENSURA) >= MINIMO_DE_CARACTER_CENSURA):
            puntos = palabra_censurada.count(CARACTER_CENSURA) * diccionario_config[PUNTOS_POR_ACIERTO]
    else:
        puntos = PUNTOS_POR_ACIERTO

    return puntos

def gano_partida(datos_jugador):
    """
    Determina si finalizó el juego o no, en base a si el usuario adivinó la
    palabra o la cantidad de desaciertos que cometió. Si el usuario ingreso
    la palabra FIN o el numero 0 tambien se termina el juego.

    Pre: Recibe la cantidad de desaciertos y el estado de la palabra a adivinar.
    Post: Devuelve True si se ha ganado el juego, o False en el caso
          contrario.
    >>> gano_partida({"palabra_a_descubrir":"casa", "palabra_censurada":"casa", "letra_a_verificar":"s"})   
    True
    >>> gano_partida({"palabra_a_descubrir":"casa", "palabra_censurada":"c?s?", "letra_a_verificar":"casa"})
    True
    >>> gano_partida({"palabra_a_descubrir":"casa", "palabra_censurada":"????", "letra_a_verificar":"o"})
    False
    """
    palabra_a_descubrir = datos_jugador["palabra_a_descubrir"]
    palabra_censurada =  datos_jugador["palabra_censurada"]
    letra_a_verificar = datos_jugador["letra_a_verificar"]

    return not (CARACTER_CENSURA in palabra_censurada) or (letra_a_verificar == palabra_a_descubrir)

def mostrar_resultado(datos_jugador, diccionario_config):
    """
    Compara el Numero de Desaciertos con el maximo tolerado; si la letra ingresada
    es una variable de corte (FIN o 0); si se ingreso toda la palabra correcta o si
    ya no quedan caracteres de censura(?). Dependiendo del caso mostrara mensajes distintos

    Pre: Recibe la cantidad de desaciertos hasta el momento(que sera un numero mayor o igual a cero),
            la palabra censurada, la letra(previamente validada), la palabra a descubrir y los puntos obtenidos
    Post: Imprime por pantalla los diferentes resultados dependiendo de como haya terminado la partida.
    """
    desaciertos = datos_jugador["desaciertos"]
    puntos = datos_jugador["puntos"]
    palabra_a_descubrir = datos_jugador["palabra_a_descubrir"]
    letra_a_verificar = datos_jugador["letra_a_verificar"]
    palabra_censurada = datos_jugador["palabra_censurada"]

    if (desaciertos == diccionario_config[MAXIMOS_DESACIERTOS]):
        print(f"\nHas perdido! Has agotado todos tus intentos :(\nLa palabra era: \"{palabra_a_descubrir}\"\n")
    elif (letra_a_verificar in CADENAS_DE_FIN):
        print(f"\nHas abandonado la partida! Suerte en la próxima!, Tus puntos son {puntos}\n")
    elif (letra_a_verificar == palabra_a_descubrir) or (not CARACTER_CENSURA in palabra_censurada):
        print(f"\nHas ganado la partida! Felicitaciones! Tus puntos son {puntos}\n"
              f"Por haber ganado la partida se te sumaran {diccionario_config[PUNTOS_ADIVINA_PALABRA]}.\n")
    elif letra_a_verificar in palabra_a_descubrir:
        print("\nHas acertado la letra!\n")
    else:
        print("\nHas terminado tu turno\n")

def puntos_finalizar_partida(datos_jugador, diccionario_ganador, nombre_turno, diccionario_config):
    """
    Incrementa los puntos al jugador que adivina la palabra.
    Caso contrario le resta a todos los jugadores por no poder adivinar la palabra.

    Pre: los diccionarios (datos_jugador) y (diccionario_ganador) no pueden estar vacios.
        El diccionario de configuracion debe tener valores para todas las variables que tenga.
    Post: Devuelve el diccionario (datos_jugador) con los puntos actualizados luego de terminar
        la partida.
    """
    if any(list(diccionario_ganador.values())):
        datos_jugador[nombre_turno]["puntos"] += diccionario_config[PUNTOS_ADIVINA_PALABRA]
    else:
        for nombre_jugador in datos_jugador.keys():
            datos_jugador[nombre_jugador]["puntos"] -= diccionario_config[PUNTOS_RESTA_GANA_PROGRAMA]
    return datos_jugador

def calcular_total(datos_jugador, datos_jugador_total, diccionario_ganador):
    """
    Se toman los puntos, aciertos y desaciertos de cada jugador del diccionario
    (datos_jugador) y se acumulan en el diccionario (datos_jugador_total) para
    tener dicha informacion.

    PRE: los 3 parametros deben ser diccionarios.
    POST: devuelve el diccionario datos_jugador_total
    """
    if not datos_jugador_total:
        for jugador, valores in datos_jugador.items():
            datos_jugador_total[jugador] = [valores["puntos"], valores["desaciertos"], valores["aciertos"]]

            if diccionario_ganador[jugador]:
                datos_jugador_total[jugador] += [1]
            else:
                datos_jugador_total[jugador] += [0]
    else:
        for jugador, valores in datos_jugador.items():
            datos_jugador_total[jugador][PUNTOS] += valores["puntos"]
            datos_jugador_total[jugador][DESACIERTOS] += valores["desaciertos"]
            datos_jugador_total[jugador][ACIERTOS] +=valores["aciertos"]
            if diccionario_ganador[jugador]:
                datos_jugador_total[jugador][CANTIDAD_PARTIDAS_GANADAS] += 1
    return datos_jugador_total

def mostrar_final_partida(datos_jugador, diccionario_ganador, diccionario_config):
    """
    Toma los datos de cada jugador del diccionario (datos jugador) e imprime por pantalla como han terminado la partida.
    Pre: Los datos del jugador no deben estar vacios, como clave debe tener el nombre de usuario, y como valor otro diccionario
        no vacio.
    Post: Imprime por pantalla los resultados de cada jugador.
    """
    print("\n---------------------------- Resumen de partida ----------------------------\n")

    for nombre_jugador, variables_juego in datos_jugador.items():
        jugador = nombre_jugador
        puntos = str(variables_juego["puntos"])
        aciertos = str(variables_juego["aciertos"])
        desaciertos =  str(variables_juego["desaciertos"])
        palabra_a_descubrir = variables_juego["palabra_a_descubrir"]
        print(f'El jugador "{jugador}" terminó la partida con {puntos} puntos. \n' + \
                f'Tuvo {aciertos} acierto/s y {desaciertos} desacierto/s.\n'+ \
                f'Su palabra a adivinar era: "{palabra_a_descubrir}"\n')

    if not any(list(diccionario_ganador.values())):
        print(f"No hubo ganador, se restan {diccionario_config[PUNTOS_RESTA_GANA_PROGRAMA]} puntos a todos los jugadores.\n")

def mostrar_final_juego(datos_jugador_total, contador_partidas):
    """
    Cuando se termina el juego, se muestran los datos de todos los jugadores
    que han participado en alguna partida. Se imprimen por pantalla los puntos
    finales que ha obtenido cada jugador, junto con sus aciertos, desaciertos y
    cantidad de partidas ganadas a lo largo del juego.

    Pre: Los datos del jugador no deben estar vacios, como clave debe tener el nombre de usuario
        y como valor otro diccionario no vacio.
    Post: imprime por pantalla los datos de cada jugador con respecto al final del juego.
    """

    jugadores_ordenados = [(resultados[PUNTOS], jugador) for jugador, resultados in datos_jugador_total.items()]
    jugadores_ordenados.sort(key=lambda item: item[PUNTOS], reverse=True)

    print("\n\n ---------------------------- Resultados Generales ----------------------------\n")
    print(f"Se jugaron un total de {contador_partidas} partida/s.\n")
    for puntos, jugador in jugadores_ordenados:
        desaciertos = datos_jugador_total[jugador][DESACIERTOS]
        aciertos = datos_jugador_total[jugador][ACIERTOS]
        cantidad_partidas_ganadas = datos_jugador_total[jugador][CANTIDAD_PARTIDAS_GANADAS]
        print(f"El jugador '{jugador}' terminó el juego con {puntos} puntos. \n" +
        f"Tuvo {aciertos} acierto/s, {desaciertos} desacierto/s, y ganó {cantidad_partidas_ganadas} partida/s.\n")

def ejecutar_ahorcado():
    """
    Contiene el código principal del programa.
    """
    contador_partidas = 0
    diccionario_config = {}

    print(SALUDO_INICIAL)

    diccionario_config = formar_diccionario_config(diccionario_config, contador_partidas)
    maximos_jugadores = diccionario_config[MAX_USUARIOS]
    listado_jugadores = ejecutar_interfaz_principal(maximos_jugadores)

    datos_jugador = generar_jugadores(listado_jugadores)

    if (len(datos_jugador) != 0):
        ejecutar_partidas(datos_jugador, maximos_jugadores, contador_partidas, diccionario_config, listado_jugadores)

    else:
        print("\nNo se ingresó ningún jugador.")

def ejecutar_partidas(datos_jugador, maximos_jugadores, contador_partidas, diccionario_config, listado_jugadores):
    """
    Contiene el bucle principal del juego que se está actualmente jugando
    """
    datos_jugador_total = {}
    diccionario_ganador = {nombre: False for nombre in datos_jugador.keys()}

    while seguir_jugando(contador_partidas):

        if (contador_partidas > PRIMER_PARTIDA):
            diccionario_config = formar_diccionario_config(diccionario_config, contador_partidas)

            if (diccionario_config[MAX_USUARIOS] != maximos_jugadores):
                maximos_jugadores = diccionario_config[MAX_USUARIOS]
                listado_jugadores = []
                datos_jugador_total = {}
                turnos_jugadores = []
                turnos_jugadores_editable = []
                diccionario_ganador = {}
                listado_jugadores = ejecutar_interfaz_principal(maximos_jugadores)
                diccionario_ganador = {nombre: False for nombre in listado_jugadores} 
                
            datos_jugador = generar_jugadores(listado_jugadores)
        
        diccionario_palabras = leer_archivos(diccionario_config)
        lista_palabras = crear_lista_ordenada(diccionario_palabras)
        largo_palabra_max = encontrar_largo_max(lista_palabras)
        escribir_archivo(lista_palabras)
        largo_palabra = indicar_largo_palabra(diccionario_config, largo_palabra_max)
        lista_palabras_candidatas = generar_lista(diccionario_palabras, largo_palabra, diccionario_config, largo_palabra_max)

        turnos_jugadores = ordenamiento_partida(diccionario_ganador, contador_partidas)
        turnos_jugadores_editable = turnos_jugadores.copy()

        datos_jugador = definir_palabras_jugadores(datos_jugador, turnos_jugadores, lista_palabras_candidatas)

        datos_jugador_total = partida_actual(datos_jugador, turnos_jugadores_editable, diccionario_config, datos_jugador_total)

        contador_partidas += 1

    mostrar_final_juego(datos_jugador_total, contador_partidas)

def partida_actual(datos_jugador, turnos_jugadores_editable, diccionario_config, datos_jugador_total):
    """
    Contiene el bucle de la partida actual
    """
    diccionario_ganador = {nombre: False for nombre in datos_jugador.keys()}
    numero_jugador = 0

    while not any(list(diccionario_ganador.values())) and (turnos_jugadores_editable != []):

        nombre_turno = turnos_jugadores_editable[numero_jugador]

        datos_jugador[nombre_turno] = turno_jugador(datos_jugador[nombre_turno], nombre_turno, diccionario_config)

        if gano_partida(datos_jugador[nombre_turno]):
            diccionario_ganador[nombre_turno] = True

        if (datos_jugador[nombre_turno]["desaciertos"] == diccionario_config[MAXIMOS_DESACIERTOS]) \
                or datos_jugador[nombre_turno]["letra_a_verificar"] in CADENAS_DE_FIN:

            turnos_jugadores_editable.remove(nombre_turno)
            numero_jugador -= 1

        numero_jugador += 1

        if (numero_jugador > len(turnos_jugadores_editable)-1):
            numero_jugador = 0

    datos_jugador = puntos_finalizar_partida(datos_jugador, diccionario_ganador, nombre_turno, diccionario_config)
    datos_jugador_total = calcular_total(datos_jugador, datos_jugador_total ,diccionario_ganador)

    mostrar_final_partida(datos_jugador, diccionario_ganador, diccionario_config)

    return datos_jugador_total

def turno_jugador(datos_jugador, nombre_turno, diccionario_config):
    """
    Contiene el bucle del turno actual
    """

    palabra_censurada_anterior = ""
    desaciertos_anterior = 0
    cambiar_turno = False

    print(f"\n---------------------------- Turno de {nombre_turno} ----------------------------\n")

    while not cambiar_turno:

        if not cambiar_turno:
            mostrar_estado(datos_jugador, nombre_turno)

        datos_jugador["letra_a_verificar"] = ingresar_letra(datos_jugador)
        datos_jugador["letras_ingresadas"] = almacenar_letras_ingresadas(datos_jugador)
        datos_jugador["aciertos"] = contar_aciertos(datos_jugador)
        desaciertos_anterior = datos_jugador["desaciertos"]
        datos_jugador["desaciertos"] = contar_desaciertos(datos_jugador)
        datos_jugador["letras_erroneas"] = almacenar_letras_erroneas(datos_jugador)
        palabra_censurada_anterior = datos_jugador["palabra_censurada"]
        datos_jugador["palabra_censurada"] = desbloquear_letra(datos_jugador)

        datos_jugador["puntos"] += calcular_puntaje(datos_jugador, desaciertos_anterior, palabra_censurada_anterior, diccionario_config)

        if (datos_jugador["desaciertos"] > desaciertos_anterior) or (datos_jugador["letra_a_verificar"] in CADENAS_DE_FIN):
            cambiar_turno = True

        if gano_partida(datos_jugador):
            cambiar_turno = True

        print("\nTus puntos son: " + str(datos_jugador["puntos"]))
        mostrar_resultado(datos_jugador, diccionario_config)

    return datos_jugador

# --------------------------- Programa Principal --------------------------- #
if __name__ == "__main__":
    print(doctest.testmod())
    ejecutar_ahorcado()
