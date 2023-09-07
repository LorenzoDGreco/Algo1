"""
Utilizando la termianl o consola de Python, realizá las siguientes operaciones:

Crea una lista con los siguientes valores, respetando el orden dado:
1  23  -100  55  48  23  -50  2  0

Inserta el valor 200 en la posición 3
Agrega a la lista el valor 35
Elimina la primer ocurrencia del valor 23
Elimina las posiciones 6,7 y 8
Agrega a la lista los valores enteros pares entre 500 y 520 inclusive
Reemplaza el valor en la posición 12, por el valor -50
Elimina el último de los elementos
Consulta cuántos elementos hay en la lista en este momento
Invierte la lista
Calcula el total de la suma de valores que forman parte de la lista e indícalo en el cuadro de texto
Suma todos los elementos que se encuentran en posiciones pares e indica el valor calculado en el cuadro de texto
"""


lista = [1,  23,  -100,  55,  48,  23,  -50,  2,  0]

lista[3] = 200

lista.append(35)

lista.remove(23)
print(lista)
lista[6:9] = []
print(lista)

for elemento in range(500, 521, 2):
    lista.append(elemento)

lista[12] = -50

lista[-1] = []

print(len(lista))

lista.reverse()

sumatoria = 0
for elemento in range(0, len(lista)):
   # print(lista[elemento]) #4650

print("-------")
sumatoria2 = 0 
for elemento in range(0, len(lista), 2):
   # print(lista[elemento])
#2202


#--------------------------
l= [2, 5, -10, 20, 50] 
l1= l[::2] #Se guarda la lista en lista1 saltando en 2 a 2
print(l,l1)
    
acumulador = 0
for posicion in range(0, len(l), 2):
    acumulador += l[posicion]
print(acumulador)
print(sum(l1)) #Suma toda la lista sin necesidad de iterar
print(sum(l[::2]))
