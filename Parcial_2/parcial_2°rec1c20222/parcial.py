FIN = "XXXXX"

def leer_archivo(archivo):
    linea = archivo.readline()
    return linea.rstrip("\n").split(",") if linea else FIN

def corte_de_control():

    ventas = open("ventas.csv", "r")
    lista_ventas = leer_archivo(ventas)

    diccionario_ventas = {}
    ventas_tot = 0
    while lista_ventas != FIN:
        dia_anterior = float(lista_ventas[0])
        ventas_dia = 0
        while lista_ventas != FIN and float(lista_ventas[0]) == dia_anterior:
            ventas_dia += float(lista_ventas[3])

            if lista_ventas[1] in diccionario_ventas:
                diccionario_ventas[lista_ventas[1]] += float(lista_ventas[3])
            else:
                diccionario_ventas[lista_ventas[1]] = float(lista_ventas[3])

            lista_ventas = leer_archivo(ventas)
        print("las ventas por día fueron de: ", ventas_dia)
        ventas_tot += ventas_dia
    print("las ventas totales fueron de: ", ventas_tot)

    return diccionario_ventas

def ordenar_ventas(diccionario_ventas):

    lista_ventas_ordenada = list(diccionario_ventas.items())

    lista_ventas_ordenada.sort(key = lambda item: item [1], reverse = True)

    return lista_ventas_ordenada

def mostrar_ventas(lista_ventas_ordenada):
    
    for elemento in lista_ventas_ordenada:
        print("El producto " + elemento[0] + " ha generado " + str(elemento[1]) + " ganancias")

diccionario_ventas = corte_de_control()

lista_ventas_ordenada = ordenar_ventas(diccionario_ventas)

mostrar_ventas(lista_ventas_ordenada)