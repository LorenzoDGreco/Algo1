total = 0
valor = int(input("Valor: "))
while valor !=0:
    total = total + valor
    valor = int(input("Valor: "))
print("Total Acumulado: ",total)

print("---------------------")

numero = int(input ("Pasa un valor del 0 al 1000 para que sea valido: "))

while (numero < 0) or (numero >= 1000):
    print ("incorrecto")
    numero = int(input ("Intnente nuevamente: "))

print("Correcto")
