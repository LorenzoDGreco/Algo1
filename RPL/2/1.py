def es_par(numero):

    if(numero % 2 == 0):
        numero_es_par = True
    else:
        numero_es_par = False
    
    return numero_es_par

def main():
    print("Es Par?: ", es_par(2))
    print("Es Par?: ", es_par(5))
    print("Es Par?: ", es_par(7))
    print("Es Par?: ", es_par(10))


main()
