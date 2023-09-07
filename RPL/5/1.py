def numeros_al_cuadrado(numero):
    diccionario = {}
    for i in range (1, numero+1):
        diccionario[i] = i**2
    return diccionario

def mezclar_diccionarios(dicc_uno, dicc_dos):
    return {**dicc_uno, **dicc_dos}
    
def filtrar_por_sumar_diez(diccionario):
    diccionario2 = {}
    for clave in diccionario:
        if diccionario[clave] + clave >= 10:
            diccionario2[clave] = diccionario[clave]
    return diccionario2
 
def ordenar_valores_por_longitud(diccionario):
    lista = []
    for clave in diccionario:
        lista.append(diccionario[clave])
    lista.sort(key = lambda item:len(item), reverse = True)
    return lista

print(numeros_al_cuadrado(4))
dicc_1 = {'clave1': 1, 'clave3': 3}
dicc_2 = {'clave2': 2, 'clave4': 4}
print(mezclar_diccionarios(dicc_1, dicc_2))
print(filtrar_por_sumar_diez({8: 11, 3: 6, 9: 2, 1: 4}))
dicc = {'boca':'river', 'pablo':'guarna', 'hola':'algoritmos'}
print(ordenar_valores_por_longitud(dicc))