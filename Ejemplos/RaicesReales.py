def Raices_Reales(a,b,c):
    resultado = (b**2) - (4*a*c)
    if (resultado >= 0):
        raices = True
    else:
        raices = False
    return raices

def main():
    a = int(input("Ingrese a: "))
    b = int(input("Ingrese b: "))
    c = int(input("Ingrese c: "))

    print(Raices_Reales(a,b,c))

main()
