num = int(input("Ingrese nota o 0 para terminar: "))
notaTot= 0
cantidad_notas = 0
while num >= 1 and num <= 11:
    notaTot = notaTot + num
    cantidad_notas = cantidad_notas + 1
    num = int(input("Ingrese nota o 0 para terminar: "))

promedio = notaTot / cantidad_notas
print("El promedio es: ", promedio)
