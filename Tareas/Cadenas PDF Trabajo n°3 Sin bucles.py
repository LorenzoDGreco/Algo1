import doctest

def esta_bien_escrito(correo):
    """
    Es la estructura principal del codigo

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
    if(not len(correo) <= 30):
        esta_bien_escrito =  False
    if esta_bien_escrito:
        esta_bien_escrito = tiene_blancos(correo, esta_bien_escrito)
    if esta_bien_escrito:
        esta_bien_escrito = tiene_letras_o_numeros(correo, esta_bien_escrito)
    if esta_bien_escrito:
        esta_bien_escrito = tiene_solo_una_arroba(correo, esta_bien_escrito)
    if esta_bien_escrito:
        esta_bien_escrito = tiene_dominio_correcto(correo, esta_bien_escrito)

        
    return esta_bien_escrito


def tiene_blancos(correo, esta_bien_escrito):
    """
    verifica si no tiene espacios en blanco
    """
    if(" " in correo):
        esta_bien_escrito = False
    return esta_bien_escrito

def tiene_letras_o_numeros(correo, esta_bien_escrito):
    """
    Verifica que no tenga caracteres alfa numericos
    """
    #si en correo de 0 hasta que se encuentre el @ crea una sub cadena
    #y pregunta si tiene letras y/o numeros si tiene un ! entonces nos da un false
    if(not correo[0:correo.find("@")].isalnum()): 
        esta_bien_escrito = False
    return esta_bien_escrito

def tiene_solo_una_arroba(correo, esta_bien_escrito):
    """
    Verifica si solo tiene una @
    """
    if correo.count("@") > 1:
        esta_bien_escrito = False
    return esta_bien_escrito

def tiene_dominio_correcto(correo, esta_bien_escrito):
    """
    Verifica si tiene bien el dominio fi.uba.ar o gmail.com
    """
    if not correo[correo.find("@"):len(correo)] == "@fi.uba.ar" and not correo[correo.find("@"):len(correo)] == "@gmail.com":
        esta_bien_escrito = False
    return esta_bien_escrito

def main():
    """
    Este es el main en donde
    se hace la llamada al resto
    de funciones
    """
    print(doctest.testmod(verbose=True))
    correo = input("Escriba su correo electronico: ")
    print(esta_bien_escrito(correo))

main()
