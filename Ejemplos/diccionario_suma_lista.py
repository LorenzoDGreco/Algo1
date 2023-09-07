"""
una duda, si tengo un diccionario:

1 : [1,2,3,4]

y digo

lista = [1,1,1,1]
diccionario[1] += lista

la respuesta es:

1: [2,3,4,5] ??

------------------------

NO, se suma [1,2,3,4,1,1,1,1]

entonces se tiene que itinerar la lista sumando elemento por elemento

"""

diccionario = {1:[1,2,3,4]}
print(diccionario)

lista = [1,1,1,1]
for clave in diccionario:
    for i in range(0,4):
        diccionario[clave][i] += lista[i]
print(diccionario)