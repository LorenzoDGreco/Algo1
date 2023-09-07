def suma_lista(lista):
    sumatoria = 0
    contador = 0
    for elemento in lista:
        contador += 1
        sumatoria += elemento
    sumatoria = sumatoria / contador
    return sumatoria

def suma_lista_positivas(lista):
    sumatoria = 0
    contador = 0
    for elemento in lista:
        if elemento >= 0:
            contador += 1
            sumatoria += elemento
    sumatoria = sumatoria/elemento
    return sumatoria

def suma_lista_1ro_ultimo(lista):
    flag = False
    primer = 0
    ultimo = 0
    for indice in range(0,len(lista)):
        if (lista[indice] < 0 and not flag):
            flag = True
            primer = indice
    flag = False
    
    for indice in range(len(lista)-1, 0, -1):
        if lista[indice] >= 0 and not flag:
            flag = True
            ultimo = indice
        
    return (lista[primer] + lista[ultimo]) / len(lista)

def ordenar_notas(lista):
    orden = sorted(lista, reverse = True)
    altas = orden[0:5]
    return altas

def notas_alumnos(lista):
    lista.sort(key = lambda x: x[1])
    return lista
#print(suma_lista([1,2,3,4,5]))
#print(suma_lista_positivas[1,2,3,4,5])
#print(suma_lista_1ro_ultimo([2, -3, 4, 100, 10, 5]))
#print(ordenar_notas([2,3,6,7,2,1,4,5,2,1]))
print(notas_alumnos([[5, "Juan Albarez"], [10,"Charly Garcia"]]))











