radio = int(input("Por favor ingrese el raido del circulo: "))

diametro = 2 * radio
area = 3.14 * (radio**2)
perimetro = 2*3.14*radio

print ("Diametro: ", diametro ,"Área: ", area ,"Perimetro: ", perimetro)

#-----------------------------------------------------------------------

palabra_1 = input("Seleccione una palabra: ")
palabra_2 = input("Seleccione otra palabra: ")
palabra_3 = input("Seleccione otra palabra: ")


print(palabra_1, palabra_2, palabra_3)
print(palabra_3, palabra_2, palabra_1)
print(palabra_2,palabra_1, palabra_3)
print(palabra_3, palabra_1, palabra_2)
print(palabra_2, palabra_3, palabra_1)
    
