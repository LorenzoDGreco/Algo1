# 1. Ya lo he hecho previamente

#-------------------------------

# 2. Es poner un if donde se pregunta si es mayor preguntando si es = al que ya hay y si lo es poner "ya ingresado" y sino que vaya a superponer la variable del máximo

# Si pide para cualquier num sin importar que sea un máximo o min.. eso ya está dificil

#--------------------------------

numero_mes = int(input("Ingrese el numero del mes que se requiera y se le dirá el nombre del mes: "))

if(numero_mes == 1):
    print("Enero")
elif(numero_mes == 2):
    print("Febrero")
elif(numero_mes == 3):
    print("Marzo")
elif(numero_mes == 4):
    print("Abril")
elif(numero_mes == 5):
    print("Mayo")
elif(numero_mes == 6):
    print("Junio")
elif(numero_mes == 7):
    print("Julio")
elif(numero_mes == 8):
    print("Agosto")
elif(numero_mes == 9):
    print("Septiembre")
elif(numero_mes == 10):
    print("Octubre")
elif(numero_mes == 11):
    print("Noviembre")
elif(numero_mes == 12):
    print("Diciembre")
else:
    print("Mes Ingresado: Invalido")
#-------------------------------

# NAH re larga y re jodida

#-------------------------------

temp = int(input("Ingrese la Temperatura: "))
unidad = input("Ingrese la unidad de la variable (C/F): ")

if(unidad == "c" or unidad == "C"):
    temp = temp + 273
    print("La temperatura en F es de: ", temp)
elif(unidad == "f" or unidad == "F"):
    temp = temp - 273
    print("La temperatura en C es de: ", temp)
else:
    print("has ingresado mal las unidades")

