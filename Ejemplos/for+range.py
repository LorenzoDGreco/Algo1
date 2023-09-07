for numero in range(1, 101):
    print (numero)

print ("------------")
print(range(6))

print ("------------")

total_pares = 0
numero = int(input("Número: "))

for par in range(2,numero+1,2):
    total_pares = total_pares + par
    print(total_pares)
print("Suma total de números pares entre 2 y ", numero, " = ",total_pares)
