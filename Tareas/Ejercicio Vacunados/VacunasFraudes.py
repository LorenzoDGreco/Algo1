#es sobre archivos secuenciales
#recorrer con while buscando un distinto, con unos if queda más complicado con los merchs
import datetime

FIN_DE_ARCHIVO = ["", "", ""]

def obtener_linea_csv(vacunados):
    linea = vacunados.readline()

    if linea == "":
        resultado = FIN_DE_ARCHIVO
    else:
        resultado = linea.rstrip().split(",")
    
    return resultado

def vacunaciones():
    vacunados = open("vacunados.csv", "r")
    infraganti = open("infraganti.txt", "w")

    linea = obtener_linea_csv(vacunados)
    while linea != FIN_DE_ARCHIVO:
        nombre, apellido, fecha = linea
        anio, mes, dia = fecha.split("-")
        fraude = False

        if (int(anio) > 2021):
            fraude = True
        elif (int(anio) == 2021 and int(mes) > 6):
            fraude = True
        elif(int(anio) == 2021 and int(mes) == 6 and int(dia) > 17):
            fraude = True

        if fraude:
            infraganti.write(f"El paciente {nombre}, {apellido} ha cometido fraude\n")
        linea = obtener_linea_csv(vacunados)
        
    vacunados.close()
    infraganti.close()

vacunaciones()

