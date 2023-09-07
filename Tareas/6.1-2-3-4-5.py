num = int(input("Ingrese un numero para factorizar: "))
numfactorizado = 1
for bucle in range (1,num+1):
    print(bucle, num,numfactorizado)
    numfactorizado = numfactorizado * bucle 

print("El resultado del factorizado es: ", numfactorizado)


#---------------------------------------------------------

num = int(input("Ingrese un numero y se le dirá si es primo o no: "))
contador = 0

for bucle in range (1, num+1):
    if((num % bucle) == 0):
        contador += 1
        print(contador)

if(contador == 2):
    print("Es Primo")
else:
    print ("No es Primo")

#---------------------------------------------------------------

num_1 = int(input("Elija su primer numero: "))
num_2 = int(input("Elija su segundo numero: "))
if(num_1 >= num_2):
    num_Mayor = num_1
else:
    num_Mayor = num_2

for bucle in range(num_Mayor,0,-1):
    if(((num_1 % bucle) == 0) and (num_2 % bucle) == 0):
        print("El MCD es: ", bucle)
        break

if(bucle == 0):
    print("No se encontro ningun MCD F")
