def precendencia_de_caracteres(cadena, caracter_1, caracter_2):
    contador = 0
    for actual in range(0,len(cadena)):
        if(cadena[actual:actual+2] == caracter_1 + caracter_2):
            contador += 1
    return contador

print(precendencia_de_caracteres("hola hola", "h", "o"))
print(precendencia_de_caracteres("la igualdad de genero es fundamental el desarrollo de una sociedad", "a", "l"))
print(precendencia_de_caracteres("la mejor verdura del universo es la pizza y el quediga lo contrario esta errado", "e", "r"))
