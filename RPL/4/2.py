def numeros_positivos(numero):
    return [x for x in range (1,numero+1)]
    
def numeros_positivos_pares(numero):
    return [x for x in range (2,numero+1,2)]
    
def numeros_positivos_pares_cuadrado(numero):
    return [x**2 for x in range (2,numero+1,2)]

def impares_al_cuadrado(lista):
    return [x**2 if not(x % 2) == 0 else x for x in lista]

def filtrar_tuplas_por_suma(lista_de_tuplas):
    return [i for i in lista_de_tuplas if i[0]+i[1]>=0]

def filtrar_tupla_elemento_par(lista_de_tuplas):
    return [i for i in lista_de_tuplas if (i[0]%2==0 or i[1]%2==0)]

print(numeros_positivos(5))
print(numeros_positivos_pares(7))
print(numeros_positivos_pares_cuadrado(7))
print(impares_al_cuadrado([1,2,3,4,5,6,7]))
print(filtrar_tuplas_por_suma([(7, -5), (4, -5), (1, 2), (1, -2)]))
print(filtrar_tupla_elemento_par([(7, -5), (4, 5), (1, 2), (1, -3), (4, 2)]))
