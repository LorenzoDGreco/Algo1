EQUIPO_DE_FUTBOL = 0
PARTIDOS_GANADOS = 1
PARTIDOS_EMPATADOS = 2
PARTIDOS_PERDIDOS = 3
PUNTOS = 1
def puntajes(lista):
    diccionario_puntajes = {}
    for elementos in lista:
        puntos = elementos[PARTIDOS_GANADOS] * 3 + elementos[PARTIDOS_EMPATADOS]
        diccionario_puntajes[elementos[EQUIPO_DE_FUTBOL]] = puntos
    return diccionario_puntajes

def printear_resultados(diccionario_puntajes):
    lista_ordenada = diccionario_puntajes.items()
    lista_ordenada = sorted(lista_ordenada, key = lambda item : item[1], reverse = True)

    for elemento in lista_ordenada:
        print("El equipo " + elemento[EQUIPO_DE_FUTBOL] + " ha sacado " + str(elemento[PUNTOS]) + " puntos")


diccionario_puntajes = {}
diccionario_puntajes = puntajes([["Boca",19,0,0], ["River",0,3,16], ["Independiente",15,4,0]])
print(diccionario_puntajes)
printear_resultados(diccionario_puntajes)