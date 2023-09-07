val_1 = int(input("Ingrese la longitud del primer lado del triangulo: "))
val_2 = int(input("Ingrese la longitud del segundo lado del triangulo: "))
val_3 = int(input("Ingrese la longitud del tercer lado del triangulo: "))

if(val_1 == val_2 and val_1 == val_3):
    print("Es equilatero")
elif(not val_1 == val_2 and (val_1 == val_3 or val_2 == val_3)) or (not val_1 == val_3 and (val_1 == val_2 or val_2 == val_3)) or (not val_2 == val_3 and (val_2 == val_1 or val_3 == val_1)):
    print("Es isosceles")
else:
    print("Es escaleno")


#--------------- Como debería de haber sido --------------------

if(val_1 == val_2 and val_1 == val_3):
    print("Es equilatero")
elif(val_1 == val_2 or val_1 == val_3 or val_2 == val_3):
    print("ta bien")
else:
    print("te fallo ameo")
