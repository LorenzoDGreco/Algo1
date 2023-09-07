def validar_contrasenia(contrasenia):
    contrasenia_validada = False
    tiene_numeros = False
    tiene_mayuscula = False
    tiene_alpha_numerico = False
    
    if 7 < len(contrasenia) and len(contrasenia) < 15:
        for caracter in contrasenia:
            if caracter.isnumeric():
                tiene_numeros = True
            if caracter.isupper():
                tiene_mayuscula = True
            if caracter.isalnum():
                tiene_alpha_numerico = True
                
    if tiene_numeros and tiene_mayuscula and tiene_alpha_numerico:
        contrasenia_validada = True
        
    return contrasenia_validada


print(validar_contrasenia("!Hola123"))
print(validar_contrasenia("Hola123"))
print(validar_contrasenia("hola123"))
print(validar_contrasenia("hola"))
print(validar_contrasenia("!Algoritmos123!Algoritmos123"))
