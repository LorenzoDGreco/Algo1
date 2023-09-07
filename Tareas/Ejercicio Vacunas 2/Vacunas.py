CORTE = '0,0,0'
FIN = '0'

def leer_info(archivo, corte):
    linea = archivo.readline()
    return linea if linea else corte

def corte_de_control():
    
    archivo = open("vacunas_otorgadas.csv","r")
    archivoEscritura = open("total_vacunas.txt", "w")

    linea = leer_info(archivo, CORTE)
    ciudad, hospital, vacunas = linea.rstrip("\n").split(",")
    total_pais = 0
    total_ciudad = 0
    total_vacunas = 0

    while ciudad != FIN:
        ciudad_ant =  ciudad
        while ciudad == ciudad_ant and ciudad != FIN:
            hospital_ant = hospital
            while hospital == hospital_ant and ciudad == ciudad_ant and ciudad != FIN:
                total_vacunas += int(vacunas)
                linea = leer_info(archivo, CORTE)
                
                ciudad, hospital, vacunas = linea.rstrip("\n").split(",")
                
            total_ciudad += total_vacunas
            archivoEscritura.write(f"Las vacunas dadas en {ciudad_ant} en el {hospital_ant} son {total_vacunas}\n")
            total_vacunas = 0

        total_pais += total_ciudad
        archivoEscritura.write(f"El total de las vacunas en {ciudad_ant} fue de {total_ciudad}\n")
        total_ciudad = 0

    archivoEscritura.write(f"El total de vacunas dadas en Argentina fue de {total_pais}\n")

    archivo.close()
    archivoEscritura.close()

corte_de_control()