def es_par (numero):
    
    if(numero % 2 == 0):
        devolver = True
    else:
        devolver = False

    return devolver

print("Es Par" if (es_par(8)) else "Es Impar")
print("Es Par" if (es_par(9)) else "Es Impar")

#------------- Vid 2 ----------------------------

def acumular_valores_rango(primer_valor, ultimo_valor):
    """
    ehto´e un komentario
    >>> acumular_valores_rango(0,4)
    10
    >>> acumular_valores_rango(-1,1)
    0
    """ 
    acumulador = 0
    for valor in range(primer_valor, ultimo_valor+1):
        acumulador += valor
        #print (valor, acumulador)
    return acumulador

"""  ----------   Bloque Principal ----------- """

print(acumular_valores_rango (0, 4))
print(acumular_valores_rango (-1 , 1))

import doctest
print(doctest.testmod())
