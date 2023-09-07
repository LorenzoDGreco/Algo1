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
    print("es_primo(1) => ", es_primo(1))
    print("es_primo(2) => ", es_primo(2))
    print("es_primo(11) => ", es_primo(11))
    print("es_primo(15) => ", es_primo(15))

main()
    
