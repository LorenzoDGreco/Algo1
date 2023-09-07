def filtrador_de_vocales(cadena):
    sin_vocales = ""
    for caracter in cadena:
        if(not caracter.lower() in "aeiouáéíóú"):
            sin_vocales += caracter
    return sin_vocales

print(filtrador_de_vocales("hola"))
print(filtrador_de_vocales("facultad"))
print(filtrador_de_vocales("algoritmos"))
