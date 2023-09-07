def validar_contrasenia(contrasenia):
    contrasenia_validada = True
    max_caracteres = 15
    min_caracteres = 7
    caracteres_actuales = len(contrasenia)
    
    if not (min_caracteres < caracteres_actuales and caracteres_actuales < max_caracteres):
        contrasenia_validada = False
    if contrasenia_validada:
        contrasenia_validada = tiene_numeros(contrasenia, contrasenia_validada)
    if contrasenia_validada:
        contrasenia_validada = tiene_mayuscula(contrasenia, contrasenia_validada)
    if contrasenia_validada:
        contrasenia_validada = tiene_no_alphanumeric(contrasenia, contrasenia_validada)
        
    return contrasenia_validada


def tiene_numeros(contrasenia, contrasenia_validada):
    if not any(chr.isnumeric() for chr in contrasenia): #Si uno solo es True devuelve True
        contrasenia_validada = False
    return contrasenia_validada

def tiene_mayuscula(contrasenia, contrasenia_validada):
    if not any(chr.isupper() for chr in contrasenia):
        contrasenia_validada = False
    return contrasenia_validada

def tiene_no_alphanumeric(contrasenia, contrasenia_validada):
    if contrasenia.isalnum():
        contrasenia_validada = False
    return contrasenia_validada

print(validar_contrasenia("!Hola123"))
print(validar_contrasenia("Hola123"))
print(validar_contrasenia("hola123"))
print(validar_contrasenia("hola"))
print(validar_contrasenia("!Algoritmos123!Algoritmos123"))
