def contar_caracteres(cadena, caracter_1, caracter_2):
    caracteres_contados = 0
    for caracter in cadena:
            if caracter.lower() in (caracter_1, caracter_2):
                caracteres_contados += 1

    return caracteres_contados


def main():

    print(contar_caracteres("Casa", "c", "a"))
    print(contar_caracteres("algoritmos", "a", "o"))

main()
