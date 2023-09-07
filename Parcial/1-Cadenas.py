def validar(cadena):
    acentos = "áéíóúÁÉÍÓÚ"
    simbolos = "*-$@"
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numeros = False
    tiene_simbolos = False
    cortar = True
    validar = False

    if len(cadena) >= 8 and len(cadena) <= 12:
        i = 0
        while (len(cadena) > i and cortar):
            if cadena[i] == " " or cadena[i] in acentos:
                cortar = False
            elif cadena[i].isupper():
                tiene_mayuscula = True
            elif cadena[i].islower():
                tiene_minuscula = True
            elif cadena[i].isnumeric():
                tiene_numeros = True
            elif cadena[i] in simbolos:
                tiene_simbolos = True
            i += 1

        if tiene_mayuscula and tiene_minuscula and tiene_simbolos and tiene_numeros and cortar:
            validar = True
        else:
            tiene_mayuscula = False

    return validar


# 8 - 12 letras, 1 mayuscula, 1 minimuscula, 1 numero,  un caracter alphanumerico ($,#,!,&,etc) y sin acentos
# Si lo tiene devuelve True sino False
print(validar("A lgoritmo$1"))
print(validar("Aprobé-con-7"))
print(validar("Algoritmo$1"))
print(validar("Aprobe-7o-s "))
