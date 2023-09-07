def suma_de_divisores(numero):
    numero_total = numero
    suma_de_divisores = 0
    for bucle in range(numero-1,1,-1):
        if((numero % bucle) == 0):
            suma_de_divisores += bucle        

    if(bucle == 0):
        suma_de_divisores = 0

    return suma_de_divisores

def main():
    

    print("suma_de_divisores(8) => ", suma_de_divisores(8))
    print("suma_de_divisores(7) => ", suma_de_divisores(7))
    print("suma_de_divisores(10) => ", suma_de_divisores(10))
    print("suma_de_divisores(31) => ", suma_de_divisores(31))
    print("suma_de_divisores(32) => ", suma_de_divisores(32))
    

main()
