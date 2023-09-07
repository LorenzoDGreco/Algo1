import doctest

def buscar_vocales(cadena):
    """
    >>> buscar_vocales("Algoritmos y programación")
    '*'
    >>> buscar_vocales("Programación1")
    'oai'
    >>> buscar_vocales("")
    '*'
    >>> buscar_vocales("+*ab")
    '*'
    >>> buscar_vocales("AÉREO")
    'AÉO'
    >>> buscar_vocales("Aereolínas")
    'Aeoí'
    >>> buscar_vocales("-P-f/7")
    '*'
    """
    vocales_finales = ""
    if (not cadena == "") or (not cadena.isalnum()):
        vocales= "aeiouáéíóú"
        for caracter in cadena:
            if caracter.lower() in vocales:
                if not caracter.lower() in vocales_finales.lower():
                    vocales_finales += caracter
        if (vocales_finales == ""):
            vocales_finales = "*"
    else:
        vocales_finales = "*"           
        
    return vocales_finales

    
print(buscar_vocales("AÉREO"))
#print(buscar_vocales("AÉREO"))
#print(doctest.testmod(verbose=True))