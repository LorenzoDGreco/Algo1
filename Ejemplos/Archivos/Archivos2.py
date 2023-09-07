# "Nico,23,342425456\n" --> rstrip("\n") --> "Nico,23,342425456\n" --split(",") --> ["Nico" , "23" , "342425456\n"]
# rstrip("\n") Derecha
# lstrip("\n") Izquierda

FIN_DE_ARCHIVO = ["", "", ""]


def obtener_linea_csv(archivo):
    linea = archivo.readline()

    if linea == "":
        resultado = FIN_DE_ARCHIVO
    else:
        resultado = linea.rstrip().split(",")

    return resultado


def main():

    archivo = open("Ejemplos\Archivos\Hola2.csv", "r")
    archivoEscritura = open("Ejemplos\Archivos\Temp.csv", "w")

    linea = obtener_linea_csv(archivo)
    while linea != FIN_DE_ARCHIVO:
        nombre, edad, dni = linea
        print(f"Nombre: {nombre}, Edad: {edad}, DNI: {dni}")
        archivoEscritura.write(f"{nombre},{int(edad) + 1},{dni}\n")

        linea = obtener_linea_csv(archivo)

    archivo.close()
    archivoEscritura.close()


main()
