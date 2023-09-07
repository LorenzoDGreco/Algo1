diccionario = {"Manuel": 18, "Pedro": 22, "Alejandro":34}

lista = []

lista = diccionario.items()

print(lista)

lista = sorted(lista, key = lambda item:item[1], reverse = True)

print (lista)