lista = [1,3,5,7,8,9,14,10]
#Quiero el 10
lista.sort()

print(lista)
print(len(lista))
"""
Primera iteracion:

inicio = inicialmente es 0
fin = inicialmente es 7
pivote = ( inicio + fin ) // 2 = 7/2 = 3,5 = 3
lista[3] == 10? No!
7 < 10? si -> se mueve el inicio al inicio = pivote + 1


Segunda iteracion:
"""

def ordenamiento_binario(lista, numero_deseado, inicio, fin):
    pivote = (inicio + fin)//2

    if inicio > fin:
        return "No encontrado"

    if lista[pivote] == numero_deseado:
        return pivote
    
    if lista[pivote] > numero_deseado:
        ordenamiento_binario(lista, numero_deseado, inicio, pivote -1)

    return ordenamiento_binario(lista, numero_deseado, pivote + 1, fin)

print(ordenamiento_binario(lista, 10, 0, len(lista)-  1))
