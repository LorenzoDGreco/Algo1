def ingresar_datos():
    candidato = ""
    diccionario = {}
    while candidato != "n":
        candidato = input("Ingrese el partido a sumarle votos: ")
        votos = int(input("Ingrese la cantidad de votos a sumarle: "))

        if candidato in diccionario:
            diccionario[candidato] += votos
        else:
            diccionario[candidato] = votos
        
        candidato = input("Desea seguir ingresando?(s/n): ")
    return diccionario

def ordenar_lista(diccionario):
    return sorted(diccionario.items(),key = lambda item:item[1], reverse = True)
     
def printear_lista_en_pantalla(lista_votaciones):
    for elemento in lista_votaciones:
        print("El partido " + elemento[0] + " obtuvo " + str(elemento[1]) + " votos.")
    return

diccionario = ingresar_datos()
lista_votaciones = ordenar_lista(diccionario)
printear_lista_en_pantalla(lista_votaciones)