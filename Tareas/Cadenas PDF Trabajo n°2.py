"""
Escribir una función que reciba una cadena de caracteres a validar,
y un segundo parámetro, que contenga una cadena con los caracteres válidos.
La función debe devolver True, si la cadena a validar, está formada sólo
por caracteres válidos; en caso contrario, deberá devolver False
"""

def validacion_de_cadena(cadena, validacion):
    """
    Compara la cadena con su validacion
    para definir si está correcta o no
    """
    return (cadena == validacion)

def main():
    #No hago un input porque es mucho trabajo escribir las 2 cadenas
    #por cada ejecucion
    print(validacion_de_cadena("Hola como estas","Hola como estas"))
    print(validacion_de_cadena("Hola como estas","estas Hola como"))
    print(validacion_de_cadena("WehT212-3sa", "WehT212-3sa"))
    print(validacion_de_cadena("WehT212-3sa", "WaTsAe-21Sa"))
    
main()

