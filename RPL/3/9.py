def sumar_caracteres_numericos(cadena):
    suma_de_numeros = 0
    for caracter in cadena:
        if(caracter.isnumeric()):
            suma_de_numeros += int(caracter)
    return suma_de_numeros


print(sumar_caracteres_numericos("1"))
print(sumar_caracteres_numericos("a1"))
print(sumar_caracteres_numericos("12"))
print(sumar_caracteres_numericos("123"))
print(sumar_caracteres_numericos("o1la293fr"))
