base = int(input("Ingrese la base: "))
potencia = int(input("Ingrese la potencia: "))
resultado = 1
for bucle in range(1, potencia+1):
    resultado = resultado * base
    
print(resultado)
