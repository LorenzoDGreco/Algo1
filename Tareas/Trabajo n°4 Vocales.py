def devolver_vocales(cadena):
    """"
    Está funcion se encarga de devolver
    las vocales que recibe del string

    >>> devolver_vocales("campana")
    'aaa'
    >>> devolver_vocales("pueblo")
    'ueo'
    >>> devolver_vocales("cg9")
    ''
    """
##    PalabraCompuesta = ""
##    for i in range(0,len(palabra)):
##        if(palabra[i] == "a"):
##            PalabraCompuesta = PalabraCompuesta + palabra[i]
##        elif (palabra[i] == "e"):
##            PalabraCompuesta = PalabraCompuesta + palabra[i]
##        elif (palabra[i] == "i"):
##            PalabraCompuesta = PalabraCompuesta + palabra[i]
##        elif (palabra[i] == "o"):
##            PalabraCompuesta = PalabraCompuesta + palabra[i]
##        elif (palabra[i] == "u"):
##            PalabraCompuesta = PalabraCompuesta + palabra[i]

    devolver = ""
    for caracter in cadena:
            if caracter.lower() in "aeiouáéíóú":
                devolver += caracter

    return devolver
    #return PalabraCompuesta


import doctest
print(doctest.testmod())
