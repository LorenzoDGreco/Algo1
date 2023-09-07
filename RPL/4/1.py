def filtrar_pares(lista):
    t = tuple(lista)
    for elemento in t:
        if not elemento % 2 == 0:
            lista.remove(elemento)
    del t
    return lista

def filtrar_primos(lista):
    t = tuple(lista)
    for elemento in t:
        if(not es_primo(elemento)):
            lista.remove(elemento)
    return lista

def es_primo(numero):
    es_primo = True 
    if numero <= 1:
        es_primo = False
    for i in range(2,numero): 
        if numero % i==0:
            es_primo= False
    return es_primo

def sumar_elementos(lista):
    sumatoria = 0
    for elemento in lista:
        sumatoria += elemento
    return sumatoria


def esta_ordenada(lista):
    lista_2 = lista[:]
    esta_ordenada = True
    lista.sort()
    if not lista == lista_2:
        esta_ordenada = False
    return esta_ordenada
    

def producto_escalar(vector_1, vector_2):
    resultado = 0
    for i in range(0,3):
        resultado += vector_1[i] * vector_2[i]
    return resultado
    

def letras_en_palabras(letras, frase):
    letras_en_palabras = True
    for elemento in letras:
        if frase.find(elemento) == -1:
            letras_en_palabras = False
    return letras_en_palabras


print(filtrar_pares([5,6,13,7,11,9,10,11]))
print(filtrar_primos([5,6,13,7,11,9,10,11]))
print(sumar_elementos([5,6,13,7,11,9,10,11]))
print(esta_ordenada([5,6,13,7,11,9,10,11]))
print(esta_ordenada([5,6,7,11]))
print(producto_escalar([2,5,3], [4,6,7]))
print(letras_en_palabras(["a","h","e"], "hola como estas"))
print(letras_en_palabras(["a","h","e"], "ola como estas"))
