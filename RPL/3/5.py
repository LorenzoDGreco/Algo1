def insertar_separadores(cadena, separador, espaciado):
    contador = 0
    caracter_separado = ""
    for caracter in cadena:
        if(contador == espaciado):
            caracter_separado += separador
            contador = 0
        caracter_separado += caracter
        contador += 1
    return caracter_separado


print(insertar_separadores("255255255255", ".", 3))
print(insertar_separadores("holacomoestas", "|", 4))
