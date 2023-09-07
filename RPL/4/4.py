def ultimos_tres_elementos(lista):
    return lista[-3:]
    
def ultimos_tres_elementos_concatenados(lista):
    return [i[-3:] for i in lista]
    
def indices_pares(lista):
    return lista[::2]
    
def indices_impares(lista):
    return lista[1::2]

def invertir(lista):
    return lista[::-1]

print(ultimos_tres_elementos([5,3,6,2,5,32,6,4,7]))
print(ultimos_tres_elementos_concatenados([[1,2,3,4], [5,6,7,8], [9,10,11,12]]))
print(indices_pares(["a","b","c","d","e"]))
print(indices_impares(["a","b","c","d","e", "f"]))
print(invertir([1,2,3,4,5]))
