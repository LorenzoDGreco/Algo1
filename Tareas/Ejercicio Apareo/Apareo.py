FIN = (0, "XXXX", 0, "X")
ID = 0
NOMBRE = 1
SUELDO = 2
MODIFICAR = 3

def leer_documento(archivo):
    """
    Estructura básica de lectra de archivos

    PRE: Debe ser un archivo de modo lectura
    POST:Lee linea por linea y devuelve una lista por los datos de la linea 
    """
    linea = archivo.readline()
    return linea.rstrip("\n").split(",") if linea != "" else FIN

def modificar_trabajador(actualizaciones_individual, nuevo_listado):
    """
    Hace las modificaciones pedidas por el archivo actualizaciones

    PRE: Las listas deben de ser [int, string, int, string], nuevo_listado
            debe ser un archivo de escritura
    POST: Se actualizarán los datos dependiendo al caracter de modificacion

    """
    if actualizaciones_individual[MODIFICAR] == "A":
        nuevo_listado.write(str(actualizaciones_individual[ID]) + " " +
        str(actualizaciones_individual[NOMBRE]) + " " +
        str(actualizaciones_individual[SUELDO] + "\n"))

    elif actualizaciones_individual[MODIFICAR] == "M":
        nuevo_listado.write(str(actualizaciones_individual[ID]) + " " +
        str(actualizaciones_individual[NOMBRE]) + " " +
        str(actualizaciones_individual[SUELDO] + "\n"))

    elif actualizaciones_individual[MODIFICAR] == "B":
        pass
    
    else:
        nuevo_listado.write("Error: La letra " + str(actualizaciones_individual[MODIFICAR]) +
                            " es invalida en el usuario " + str(actualizaciones_individual[NOMBRE]) + "\n")

def no_modificar_trabajador(trabajador_individual, nuevo_listado):
    """
    Mantiene los datos del trabajador sin modificar

    PRE: Las listas deben de ser [int, string, int, string], nuevo_listado
            debe ser un archivo de escritura
    POST: Escribe los datos del trabajador
    """
    nuevo_listado.write(str(trabajador_individual[ID]) + " " +
    str(trabajador_individual[NOMBRE]) + " " +
    str(trabajador_individual[SUELDO] + "\n"))

def main():
    """
    Codigo Principal

    PRE: Los archivos CSV: trabajadores y actualizaciones deben existir
    """
    trabajadores = open("trabajadores.csv", "r")
    actualizaciones = open("actualizaciones.csv", "r")
    nuevo_listado = open("nuevo_listado.txt", "w")

    trabajador_individual = leer_documento(trabajadores)
    actualizaciones_individual = leer_documento(actualizaciones)

    while trabajador_individual[ID] != FIN[0] and actualizaciones_individual[ID] != FIN[0]:
        if trabajador_individual[ID] == actualizaciones_individual[ID]:
            modificar_trabajador(actualizaciones_individual, nuevo_listado)
            trabajador_individual = leer_documento(trabajadores)
            actualizaciones_individual = leer_documento(actualizaciones)

        elif trabajador_individual[ID] < actualizaciones_individual[ID]:
            no_modificar_trabajador(trabajador_individual, nuevo_listado)
            trabajador_individual = leer_documento(trabajadores)

        elif trabajador_individual[ID] > actualizaciones_individual[ID]:
            modificar_trabajador(actualizaciones_individual, nuevo_listado)
            actualizaciones_individual = leer_documento(actualizaciones)

    while trabajador_individual[ID] != FIN[ID]:
        no_modificar_trabajador(trabajador_individual, nuevo_listado)
        trabajador_individual = leer_documento(trabajadores)

    while actualizaciones_individual[ID] != FIN[ID]:
        modificar_trabajador(actualizaciones_individual, nuevo_listado)
        actualizaciones_individual = leer_documento(actualizaciones)

    trabajadores.close()
    actualizaciones.close()
    nuevo_listado.close()
main()