#------------- Vid 2 ----------------------------

def acumular_valores_rango(primer_valor, ultimo_valor):
    
    acumulador = 0
    for valor in range(primer_valor, ultimo_valor+1):
        acumulador += valor
        print (valor, acumulador)
    return acumulador

#  ----------   Bloque Principal ----------- 

print(acumular_valores_rango (0, 4))
print(acumular_valores_rango (-1 , 1))
