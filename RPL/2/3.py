def es_potencia_de_dos(numero):
    es_potencia_de_dos = True
    
    if numero < 1:
        es_potencia_de_dos = False
    elif numero <= 2:
        es_potencia_de_dos = True
    else:
        i = 2
        while not i == 0:
            i *= 2
            if i == numero:
                es_potencia_de_dos = True
                i = 0
            if i > numero:
                es_potencia_de_dos = False
                i = 0
    return es_potencia_de_dos


def main():
    print("es_potencia_de_dos(1) =>", es_potencia_de_dos(1))
    print("es_potencia_de_dos(2) =>", es_potencia_de_dos(2))
    print("es_potencia_de_dos(3) =>", es_potencia_de_dos(3))
    print("es_potencia_de_dos(4) =>", es_potencia_de_dos(4))
    print("es_potencia_de_dos(15) =>", es_potencia_de_dos(15))
    print("es_potencia_de_dos(16) =>", es_potencia_de_dos(16))
    print("es_potencia_de_dos(30) =>", es_potencia_de_dos(30))
    print("es_potencia_de_dos(32) =>", es_potencia_de_dos(32))


main()
