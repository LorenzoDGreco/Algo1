def es_primo(numero):
    es_primo = True 
    if numero <= 1:
        es_primo = False
    for i in range(2,numero): 
        if numero % i==0:
            es_primo= False
    return es_primo

def filtrar_primos(numeros, menor_numero):
    return [i for i in numeros if es_primo(i) and i > menor_numero]

def ordenar_por_longitud_de_tuplas(tuplas):
    return sorted(tuplas, key = lambda item: len(item), reverse = True)

def concatenar_primeros_elementos(lista):
    #return [i[:2] for i in lista] A mi me gusta así pero el rpl no me deja
    lista_final = []
    for elemento in lista:
        sub_elemento = elemento[:2]
        for numero in sub_elemento:
            lista_final.append(numero)
    return lista_final
    
    
print(filtrar_primos([3, 7, 11, 13], 8))
print(filtrar_primos([11, 7, 3, 19], 15))
lista_tuplas = [(1,5,6), (1,2), (1,), (6,4,5,6), ("asd", 9, 5.6, "l", "s")]
print(ordenar_por_longitud_de_tuplas(lista_tuplas))
lista = [[1,4,5,6], [2,3,4,5], [6,4,4,6,7,8], [5,6,7,3,5,6,4]]
print(concatenar_primeros_elementos(lista))
