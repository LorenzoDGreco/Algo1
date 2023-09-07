"""Escribir una función que reciba una cadena de caracteres.
La función deberá evaluar si la cadena recibida
representa un número binario, y en ese caso devolver True,
de lo contrario, deberá devolver False.

No se pueden utilizar ninguno de los métodos tales como
isnumeric, isalpha, isalnum.
Se debe evitar la realización de ciclos innecesario,
mediante la aplicación del ciclo correcto.
"""

import doctest

def es_numero_binario(numero):
    """
    Esta funcion se fija en todos los caracteres
    si el numero ingresado es 1 o 0

    >>> es_numero_binario("0A101010111111111011111011111110")
    False
    >>> es_numero_binario("011101")
    True
    >>> es_numero_binario("")
    False
    >>> es_numero_binario("1")
    True
    >>> es_numero_binario("0")
    True
    """
    es_numero_binario = False
    contador = 0
    if(numero == ""):
        contador -= 1
    else:
        for caracter in numero:
                if(caracter == "0" or caracter == "1"):
                    contador += 1

        if(len(numero) == contador):
            es_numero_binario = True
    
    return es_numero_binario


def main():
    print(doctest.testmod())
    numero = input("Escriba un codigo binario: ")
    print(es_numero_binario(numero))

main()
