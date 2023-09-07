Lista_vacia = []
lista = []
lista.append("Juan")
lista.append("Perez")
print(lista)
#['Juan', 'Perez']
#   0        1
#  -2      -1
print(lista[1])

lista += ["Pedro"]
print(lista)

lista.insert(1, 15)
print(lista)

del(lista[1])
print(lista)

juan = ""
juan = lista.pop(0)
print(lista)
print(juan)

#lista.remove("Juan")
#print(lista)
lista += ["Juancho", "Azul"]
lista_min = min(lista)
lista_max = max(lista)
print(lista)
print(lista_min)
print(lista_max)

print(lista.count("Pedro"))

lista = [4,6,1,10]
lista.sort(reverse = True)
print(lista)

lista1 = sorted(lista)
print(lista)
print(lista1)

lista1 = lista[:] #una nueva lista idependiente y modificable

#t = tuple()
#for i in t
#    if hfytfy
lista=[1, 1, 3, 4, 8, 10]
for i in lista:
    if i % 2 == 0:
        lista.remove(i)
print(lista)

for indice,elemento in enumerate(lista):
    print(indice, elemento)
    
#Desempaquetado
persona = ["Juan", "Perez", 15]
nombre, apellido, edad = persona
print(nombre)
print(apellido)
print(edad)

#Compresion
numeros_hasta_el_100 = [x for x in range(1,101)]
print(numeros_hasta_el_100)

numeros_par_entre_1_y_100 = [x for x in range(1,101) if x%2==0]
print(numeros_par_entre_1_y_100)


lista = [["Juan", "Perez"],["Emilia", "Juanes"]]
lista1 = sorted(lista, reverse = True, key = lambda x:x[1])
print(lista1)
