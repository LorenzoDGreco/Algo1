def devolver_cadena(cadena):
    cadena_final = ""
    signos_ignorar = "[](){},;:"
    if not cadena.isalpha():
        for caracter in cadena:
            if not caracter.isalpha() and not caracter in cadena_final:
                if caracter.isnumeric():
                    cadena_final += caracter
                elif not caracter in signos_ignorar:
                    cadena_final += caracter
                else:
                    cadena_final += ""
    return cadena_final

print(devolver_cadena("{[(a+b)]}*15"))
print(devolver_cadena("+*ab"))
print(devolver_cadena("según:1.1;1.2;1.3."))
print(devolver_cadena("-P-f/7"))