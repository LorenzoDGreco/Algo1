"""
Es interesante como se recorre 
la lista de este sentido <- (de n mayor a menor)
cuando uno quiere sumar el
 5,2,... (Osea de n menor a mayor)
entonces por los return queda una especie
de pila tipo lifo haciendo que se sume 
de sentido contrario entonces así si queda
de este sentido ->
"""
 
def sumar(lista, n):
    if n == 0:
        return 0
    return lista[n-1] + sumar(lista,n-1)

print(sumar([5,2,6,23,4], 3))
print(sumar([5,2,6,23,4], 1))
print(sumar([5,2,6,23,4], 0))
print(sumar([5,2,6,23,4], 5))
