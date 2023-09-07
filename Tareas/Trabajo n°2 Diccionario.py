def lista_equipos():
    
    diccionario={}
    
    equipo=input("ingrese el nombre del equipo (enter para terminar) :")
    
    while equipo!= "":
        print("")
        puntos = int(input("ingrese los puntos del equipo: "))
        
        if equipo in diccionario:
            diccionario[equipo]+=puntos
        
        else:
            diccionario[equipo] = puntos
        
        print("")
        equipo = input("Ingrese otro equipo: ")
    
    lista_ordenada = diccionario.items()
    
    return sorted(lista_ordenada, key = lambda item : item[1], reverse = True)

print(lista_equipos())
