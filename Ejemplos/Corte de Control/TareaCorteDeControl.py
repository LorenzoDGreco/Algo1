def leer_info(archivo, corte):
    linea = archivo.readline()
    return linea if linea else corte

def corte_de_control():
    CORTE = "-1" # R > 0
    
    archivo = open("txt.csv","r")
    archivoEscritura = open("Temp.csv", "w")

    linea = leer_info(archivo, CORTE)
    cuil, fecha_venta, codigo, cantidad, precio = linea.rstrip("\n").split(",")
    total = 0
    while cuil != CORTE:   
        cuil_ant = cuil
        total_cuil = 0
        while cuil == cuil_ant and cuil != CORTE:
            total_cuil += int(cantidad) * int(precio)
            linea = leer_info(archivo, CORTE)
            try:
                cuil, fecha_venta, codigo, cantidad, precio = linea.rstrip("\n").split(",")
            except:
                cuil = CORTE
        archivoEscritura.write("El total del CUIL " + cuil_ant + " es " + str(total_cuil) + "\n")
        total += total_cuil
    archivoEscritura.write("Total General: " + str(total))
    archivo.close()
    archivoEscritura.close()

corte_de_control()