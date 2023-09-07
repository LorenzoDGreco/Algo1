def tiene_diptongo(palabra):
    #la transformo en una lista
    lista = []
    for caracter in palabra:
        lista.append(caracter)        

    es_diptongo = False
    if "i" in lista:
        es_diptongo = anti_crash("i", es_diptongo, lista)
    if "u" in lista:
        es_diptongo = anti_crash("u", es_diptongo, lista)
    return es_diptongo

def anti_crash(caracter, es_diptongo, lista):
    abiertas = "aeo"
    posicion = lista.index(caracter)
    if lista[posicion+1] in abiertas:
        es_diptongo = True
    elif lista[posicion-1] in abiertas:
        es_diptongo = True
    return es_diptongo

def main():
    #Presupongo que me lo dan una PALABARA en un string
    palabra = input("Ingrese su palabra con diptongo: ")
    print(tiene_diptongo(palabra))
    
main()
