# BUSQUEDA SECUENCIAL
def indice(lista, numero):
    resultado = False
    if numero in lista:
        resultado = lista.index(numero)
    return resultado

lista = [5,8,1,9,5,-2]

print(indice(lista, 9))
print(indice(lista, 8))
print(indice(lista, 3))

print("-----------")

#Busqueda secuencial con corte
def busqueda(lista,numero):
    resultado = -1
    i = 0
    while resultado == -1 and i < len(lista):
            if lista[i]==numero:
                resultado = i
            i += 1
    return resultado

lista = [5,8,1,9,5,-2]

print(busqueda(lista, 5)) # Este codigo en busqueda "5" tiene un coste 1, este es el mejor caso
print(busqueda(lista, -2))# Este tiene un costo 6
print(busqueda(lista, 3))
#en N valores tendré N costes
#Este codigo tiene nombre o(n), Osea Orden N


print("-----------------")

#Busqueda secuencial con lista ordenada
def busqueda2(lista,numero):
    resultado = -1
    i = 0
    while i < len(lista) and lista[i] < numero:
        if lista[i]==numero:
            resultado = i
        i += 1
        if i < len(lista) and lista[i] == numero:
            resultado = i
    return resultado

lista = [-2,1,5,5,8,9]

print(busqueda2(lista, 3))
print(busqueda2(lista, 5))
print(busqueda2(lista, 9))
# O(n) este codigo es mejor al anterior pero en el peor de los casos igual de malo que el anterior

print("-----------")

def busqueda_binaria(lista, valor):
    inf = 0
    sup = len(lista)
    encontrado = False
    while not encontrado and inf <= sup:
        medio = (inf + sup) //2
        if lista[medio] == valor:
            encontrado = True
        elif lista[medio] > valor:
            sup = medio - 1
        else:
            inf = medio + 1
    if not encontrado:
        medio = -1
    return medio

lista = [-2,1,5,6,8,9,15,21,23]

print(busqueda_binaria(lista, 3))
print(busqueda_binaria(lista, 5))
print(busqueda_binaria(lista, 9))
print(busqueda_binaria(lista, 11))
# O(log n)

print("------------")

def seleccion(lista):
    n = len(lista)
    for i in range(n - 1):
        pos_min = i
        for j in range(i+1, n):
            if(lista[j] < lista[pos_min]):
                pos_min = j
        intercambiar(lista, i, pos_min)

def intercambiar(lista, i, pos_min):
    aux = lista[i]
    lista[i] = lista[pos_min]
    lista[pos_min] = aux

def main():
    lista = [5,1,8,11,3,-2,6]
    print(lista)
    seleccion(lista)
    print (lista)

main()
#O(n2) Ordenamiento N al cuadrado

print("------------")

# Burbujeo

def burbujeo(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(1, n-i):
            if(lista[j-1] > lista[j]):
                intercambiar2(lista, j-1, j)

def intercambiar2(lista, i, pos_min):
    aux = lista[i]
    lista[i] = lista[pos_min]
    lista[pos_min] = aux



def main():
    lista = [5,1,8,11,3,-2,6]
    print(lista)
    burbujeo(lista)
    print (lista)

main()
#O(n2) Ordenamiento N al cuadrado

print("------")

# Inserción

def insercion(lista):
    n = len(lista)
    for i in range(1, n):
        auxiliar = lista[i]
        j = i
        while ((j > 0) and (lista[j - 1] > auxiliar)):
            lista[j] = lista[j - 1]
            j = j - 1
        lista[j] = auxiliar

# def insercion(lista):
#     for i in range(len(lista)):
#         for j in range(i,0,-1):
#             if(lista[j-1] > lista[j]):
#                 aux=lista[j]
#                 lista[j]=lista[j-1]
#                 lista[j-1]=aux

def main():
    lista = [5,1,8,11,3,-2,6]
    print(lista)
    insercion(lista)
    print (lista)

main()
# O(n2/2) Ordenamiento de n al cuadrado dividido 2