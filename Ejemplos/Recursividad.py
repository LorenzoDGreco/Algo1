#La recursividad es una funcion que se llama a si misma
#Pero esto no es una recursividad, porque no tiene sus 3 bloques
#Cuales son Condiciopn de corte, bloque de acciones, llamado a si misma

# def funcion():
#     funcion()
# funcion()


#Lo que falla es que si ingreso otro numero que no sea 5 entro en bucle infinito


def funcion2(numero):
    if numero == 5:
        return numero
    funcion2(numero)

print(funcion2(5))

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente -1)

print(potencia(3,5))

def fibonacci(orden):
    if orden == 0:
        return 0
    if orden == 1:
        return 1
    return fibonacci(orden-1) + fibonacci(orden-2)

fibonacci(6)

def factorial(factor):
    if factor == 0:
        return 1
    return factor * factorial(factor - 1)

print(factorial(5))

def crear_lista(lista, numero_agregar):
    
    if numero_agregar == 0:
        return lista
    lista.append(numero_agregar)
    return crear_lista(lista, numero_agregar - 1)

lista = []
print(crear_lista(lista,5))
