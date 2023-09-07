Gravedad = float(input("Ingrese el valor de la gravedad: "))
Peso = float(input("Ingrese su peso: "))

if(Gravedad >= 5):
    print("Alerta, gravedad peligrosamente alta")

Peso_Calculado = (Gravedad * Peso) / 9.807


print ("Su peso seria: " + "{:.2f}".format(Peso_Calculado) + " kg")