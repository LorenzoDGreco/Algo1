lista = [2, 23, 8, 48, 5, 0]
print(lista)
print(lista.index(2)) # Me tira la posicion 0 que se encuentra el numero 2

print("---------")

lista = [235, "azul", 28.3, "rojo"]
#        0       1     2      3

print(lista)
print(len(lista)) # Me tira la cantidad de valores totales que posee la lista
print(lista[3])  #Lee de izq a der
print(lista[-2]) #Lee de der a izq

print("------")

lista2 = [2, 3]

listaTot = lista + lista2 # Sumo las listas poniendo la segunda al final

print(listaTot)

print("------")

lista = [2, 23, 8, 30]
print(lista)
lista[2] = 53 # Ingresa el valor 53 en la posicion 2
print(lista)
lista.append(-15) #Agrega al final un -15
print(lista)
lista += [6] #otra forma de agregar algo al final
print(lista)
#sumo 6 + 6
lista[5] += 6 #Suma en la posicion 5 un 6 entonces 6+6=12
print(lista)
#lista = lista.extend(range(0,2)) Me tira error
#print(lista)

lista.insert(0, -20) #inserta en la posicion 0 un -20 y corre al resto
print(lista)

#print(del(lista[0])) elimina el valor de la lista
valor = 0
valor = lista.pop(2) #lo quita y se lo da a la variable 
print(lista, valor)

lista.remove(-15) #en esta version explota
print(lista)      #Remueve el valor -15 en cualquier parte de la lista

#lista.clear() ME BORRRA TODO AAAAA

print(lista.count(-20))

lista.reverse() #pone al reves la lista
print(lista)

lista.sort() #lo pone de menor a mayor
print(lista) #sorted para que no me cambie la lista

print(lista[0:4]) #sería del 0 al 3, es un 4 trucho
print(lista[-5:-1]) #lo mismo pero de der a izq


print(lista)
lista[2:4] = [] #Borra de 2 a 4 todo lo que tiene
print(lista)

for elemento in range(0, len(lista)): #printear una lista
    print(lista[elemento])

#for elemento in lista:     Correcto pero tira error en esta version 
#    print(lista[elemento])

lista = [] #Generar una lista desde 0
for x in range(1,10):
    lista.append(x**2)
    print(lista)

print("-------")

l= [2, 5, -10, 20, 50] 
l1= l[::2] #Se guarda la lista en lista1 saltando en 2 a 2
print(l,l1)
    
acumulador = 0 #Suma todos los componentes de la lista
for posicion in range(0, len(l), 2):
    acumulador += l[posicion]
print(acumulador)

print(sum(l1)) #Suma toda la lista sin necesidad de iterar
print(sum(l[::2]))

print("-----")

lista = [1,2,3,4,5,6,7,8]

lista = [x**2 for x in range(1,10)] #Declarar un for dentro de una lista, re flashero
print(lista)

lista = [x+2 for x in range(1,10)]
print(lista)

l_super = [["jabón",10],["agua mineral",5],["vinos",1]]
print(l_super[2])
print(l_super[0][1])
print(l_super[1][0]) 

l_alumn_notas = [["Juan Perez",[4,3,7]],["Julieta Garcia",[8,6]],["Gabriel Dias",[]]]
print(l_alumn_notas[1][1])


l_super.sort() #Acomoda la lista pero con el primer valor
print(l_super)

l_super.sort(key = lambda item : item[1]) #acomodas la lista con los valores que le das
print(l_super)

print("-------")

suma = lambda x,y : x+y
print(suma(5,8))

#short if con lamdba fijarse en google

l= [1,7,10,15,3] #Distintas formas para no compartir una lista
l1 = l #Se comparte
l2 = list(l) #no se comparte
t = tuple(l) #no se comparte

print(l,l1,t,l2)

del(l[0]) #Aca borro la primera posicion para verificar que es lo que cambia
print(l,l1,t,l2)
