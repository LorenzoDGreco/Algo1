"""
Escribir una función que reciba una dirección de mail,
y devuelva True ó False, en función de haber
evaluado que dicha dirección está bien formada.

Escribir una función que reciba una cadena de caracteres
que representa una dirección de mail. La función deberá
devolver True ó False, en función de haber evaluado que
dicha dirección está bien formada.

Se debe controla que:
a. Que no contenga blancos
b. Que sólo se utilicen letras y/o números
    para la parte del nombre, delante de la @
c. Que haya exactamente una arroba
d. Que los nombres de dominio sean: fi.uba.ar ó gmail.com
"""
import doctest
contador_de_arrobas = 0

def esta_bien_escrito(correo):
    """
    Esta es la estrucura principal

    >>> esta_bien_escrito("jperez@fi.uba.ar")
    True
    >>> esta_bien_escrito("j perez@fi.uba.ar")
    False
    >>> esta_bien_escrito("j_perez@fi.uba.ar")
    False
    >>> esta_bien_escrito("jperez@hotmail.com")
    False
    >>> esta_bien_escrito("juanaugustolisandroperezgarciafernandez@fi.uba.ar")
    False
    """
    esta_bien_escrito = True
    
    i = 0
    if(len(correo) <= 30):
        while esta_bien_escrito == True and len(correo) > i:
            
            if esta_bien_escrito:
                esta_bien_escrito = tiene_blancos(correo[i], esta_bien_escrito)

            if esta_bien_escrito:
                esta_bien_escrito = tiene_letras_o_numeros(correo[i], esta_bien_escrito)

            if esta_bien_escrito:
                esta_bien_escrito = tiene_solo_una_arroba(correo[i], esta_bien_escrito)
                
            i += 1
        
        if esta_bien_escrito:
            esta_bien_escrito = tiene_dominio_correcto(correo, esta_bien_escrito)

    else:
        esta_bien_escrito = False
        
    return esta_bien_escrito

def tiene_blancos(caracter, esta_bien_escrito):
    
    if(caracter == " "):
        esta_bien_escrito = False
    return esta_bien_escrito

def tiene_letras_o_numeros(caracter, esta_bien_escrito):
    if(not caracter == "@" and not caracter == "."):
        if(not caracter.isnumeric() and not caracter.isalpha()):
            esta_bien_escrito = False
    return esta_bien_escrito

def tiene_solo_una_arroba(caracter, esta_bien_escrito):
    global contador_de_arrobas
    if(caracter == "@"):
        contador_de_arrobas += 1
    if(contador_de_arrobas > 1):
        esta_bien_escrito = False
    return esta_bien_escrito

def tiene_dominio_correcto(correo, esta_bien_escrito):
    dominio_actual = ""
    for caracter in range(correo.find("@"), len(correo)):
        dominio_actual += correo[caracter]
    if not dominio_actual == "@fi.uba.ar" and not dominio_actual == "@gmail.com":
        esta_bien_escrito = False
    return esta_bien_escrito

def main():
    #print(doctest.testmod(verbose=True))
    correo = input("Escriba su correo electronico: ")
    print(esta_bien_escrito(correo))

main()
