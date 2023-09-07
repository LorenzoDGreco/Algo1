# Tarea n°1 Decir el número mayor y menor ingresado

# Interfaz de Usuario

ID = 1
print("Seleccione numeros y este programa le dirá los menores y mayores: \n")
print("Elija ", ID, "° número (Seleccione 'salir' para finalizar): ", end=" ")
numero = input()

if (numero != "salir"):
    numero = int(numero)
    menorTot = numero  # Seteo variables para tener el punto de inicio
    mayorTot = numero

    numero = str(numero)

    while numero != "salir":
        numero = int(numero)  # Vuelvo a guardar el resultado en int
        ID += 1

        # Parte logíca
        if (numero >= mayorTot):
            mayorTot = numero

        if (numero <= menorTot):
            menorTot = numero

        print("Elija ", ID, "° número (Seleccione 'salir' para finalizar): ", end=" ")
        numero = input()

        numero = str(numero)  # Para que detecte el "salir"
elif (numero == "salir"):
    menorTot = "Sin Resultados"
    mayorTot = "Sin Resultados"

print("El menor es: ", menorTot)
print("El mayor es: ", mayorTot)
