def ordenar(lista, sentido):
    if sentido == 1:
        largo_lista = len(lista) - 1

        #bucle que avanza
        for i in range(largo_lista):

            #bucle que hace comparaciones e intercambios
            for j in range(largo_lista):
                if(lista[j] > lista[j+1]):
                    intercambiar(lista, j)

    if sentido == 2:
        largo_lista = len(lista) - 1

        #bucle que avanza
        for i in range(largo_lista):

            #bucle que hace comparaciones e intercambios
            for j in range(largo_lista):
                if(lista[j] < lista[j+1]): #solo esto cambia, increible
                    intercambiar(lista, j)

    return lista

def intercambiar(lista, j):
    auxiliar = lista[j]
    lista[j] = lista[j+1]
    lista[j+1] = auxiliar

print(ordenar([11, 2, 16, 8], 1))
print(ordenar([11, 2, 16, 8], 2))