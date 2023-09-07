def main():

    print("hola, %s!" %"Nicolas")

    numero = 3.15463185

    print("Imprimo número al final: ", numero)
    print("Imprimo número al final concatenado: " + str(numero))
    print("Imprimo 2 número en el medio de la string {} {}, lo agregué con format".format(numero,numero ** 2))
    print("Imprimo 2 número en el medio de la string {1} {0}, lo agregué con format".format(numero,numero ** 2))
    #                               Son las posiciones 0 primero 1 segundo
    print(f"Utilizo fstring para imprimir el número {numero} en la cadena")
    print("imprimo número con 2 decimales: {:.2f}".format(numero))






main()
