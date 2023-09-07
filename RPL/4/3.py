def ordenar_lista_menor_a_mayor(lista):
    return sorted(lista)


def ordenar_lista_mayor_a_menor(lista):
    return sorted(lista, reverse=True)


def ordenar_lista_alfabeticamente(lista):
    return sorted(lista)


def ordenar_palabras_por_longitud(lista):
    return sorted(lista, key=len, reverse=True)


def ordenar_lista_por_tupla(lista):
    return sorted(lista, key=lambda x: x[1], reverse=True)


def ordenar_lista_por_suma_tupla(lista):
    return sorted(lista, key=lambda x: x[0]+x[1], reverse=True)


# def ordenar(lista):
#     return sorted(lista, key=lambda x: x[1])


print(ordenar_lista_menor_a_mayor([5, 2, 6, 23, 4]))
print(ordenar_lista_mayor_a_menor([5, 2, 6, 23, 4]))
print(ordenar_lista_alfabeticamente(["hola", "estas", "como", "si"]))
print(ordenar_palabras_por_longitud(
    ["a", "hola", "si", "string largo", "string"]))
print(ordenar_lista_por_tupla([(1, 2), (2, 3), (6, 7), (5, 4), (7, 1)]))
print(ordenar_lista_por_suma_tupla([(1, 5), (7, 3), (5, 4), (4, 3)]))


# print(ordenar([[4, ["Ana", "ambar"]], [1, ["Sna", "Smbar"]],[6, ["Zna", "Zmbar"]], [2, ["Cna", "cmbar"]]]))
