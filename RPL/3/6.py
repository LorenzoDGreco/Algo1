def palabra_mas_larga(texto):
    palabra_mas_larga = ""
    palabra_actual = ""
    
    for caracter in texto:
        if(caracter == " "):
            if (len(palabra_mas_larga) < len(palabra_actual)):
                palabra_mas_larga = ""
                palabra_mas_larga = palabra_actual
            palabra_actual = ""
        else:
            palabra_actual += caracter

    #Este ultimo if existe para confirmar la ultima palabra
    if (len(palabra_mas_larga) < len(palabra_actual)):
        palabra_mas_larga = ""
        palabra_mas_larga = palabra_actual
    
    return palabra_mas_larga


def main():
    print(palabra_mas_larga("Hola como estas este es un texto de prueba"))
    print(palabra_mas_larga("Quiero aprobar algoritmos y algebra"))

main()
