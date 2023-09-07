def suma_de_numeros_primos(numero):
    suma_de_numeros_primos = 0

    for i in range(2,numero+1):
        if(es_primo(i) == True):
            suma_de_numeros_primos += i

    return suma_de_numeros_primos

def es_primo(numero):
    contador = 0
    for bucle in range (1, numero+1):
        if((numero % bucle) == 0):
            contador += 1

    if(contador == 2):
        es_primo = True
    else:
        es_primo = False

    return es_primo

def main():
    print("suma_de_numeros_primos(1) => ", suma_de_numeros_primos(1))
    print("suma_de_numeros_primos(2) => ", suma_de_numeros_primos(2)) 
    print("suma_de_numeros_primos(3) => ", suma_de_numeros_primos(3))
    print("suma_de_numeros_primos(4) => ", suma_de_numeros_primos(4))
    print("suma_de_numeros_primos(5) => ", suma_de_numeros_primos(5))
    print("suma_de_numeros_primos(17) => ", suma_de_numeros_primos(17))

main()
