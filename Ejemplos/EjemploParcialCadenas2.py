def validar(cadena):
    contador_0 = 0
    i = 0
    validada = False
    if (len(cadena) >= 4 and len(cadena) <= 8) and cadena.isnumeric():
        while i < len(cadena) and contador_0 < 2:
            if cadena[i] == "0":
                contador_0 += 1
            if len(cadena)-1 == i and contador_0 < 2:
                validada = True
            i += 1 
    return validada

print(validar("j2020"))
print(validar("2021a"))
print(validar("20X21"))
print(validar("2220"))
print(validar("23445776"))
print(validar("089"))
print(validar("027845321"))
print(validar("02784532"))
print(validar("303330"))
