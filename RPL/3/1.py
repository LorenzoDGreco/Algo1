def longitud_cadenas(cadena_1, cadena_2, cadena_3):
    cadena_compuesta = cadena_1 + cadena_2 + cadena_3
    total_cadena = 0
    for i in cadena_compuesta:
        total_cadena += 1
    
    return total_cadena

def longitud_cadenas_correcta(cadena_1, cadena_2, cadena_3):
    return len(cadena_1 + cadena_2 + cadena_3)

def main():

    print(longitud_cadenas_correcta("hola", "como", "estas"))

main()
