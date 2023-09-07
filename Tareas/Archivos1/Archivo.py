"""
Buscar todas las vocales y ponerles un acento
"""

def iterar_lineas(archivo):
    texto = ""
    for linea in archivo:
        for caracter in linea:
            if caracter in "aeiou":
                texto += reemplazar_vocales(caracter, texto)
            else:
                texto += caracter
    return texto

def reemplazar_vocales(caracter, texto):
    if caracter == "a":
        caracter = "á"

    elif caracter == "e":
        caracter = "é"
            
    elif caracter == "i":
        caracter = "í"
            
    elif caracter == "o":
        caracter = "ó"
            
    elif caracter == "u":
        caracter = "ú"

    return caracter

def main():
    archivo = open("texto.txt", "r")
    archivofin = open("texto_con_acentos.txt", "w")

    texto = iterar_lineas(archivo)
    archivofin.write(texto)

    archivo.close()
    archivofin.close()

main()