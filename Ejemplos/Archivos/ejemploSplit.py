def obtener_linea_csv(linea):

    if linea == "":
        resultado = []
    else:
        resultado = linea.rstrip().split(",")
    
    return resultado
    
print(obtener_linea_csv("Nico,24,342425456"))