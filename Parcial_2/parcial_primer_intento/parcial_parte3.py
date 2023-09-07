FIN = "XXXXX"
DIA = 0
PRODUCTO = 1
VENTAS = 2
NOMBRE = 0
STOCK = 1

def leer_linea(archivo):
    linea = archivo.readline()
    return linea.rstrip("\n").split(",") if linea else FIN

def armado_merge():
    ventas1 = open("ventas1.csv", "r")
    ventas2 = open("ventas2.csv", "r")

    resultante = open("resultante.csv", "w")

    lista_venta1 = leer_linea(ventas1)
    lista_venta2 = leer_linea(ventas2)

    while lista_venta1 != FIN or lista_venta2 != FIN:

        minimo = min(lista_venta1[DIA], lista_venta2[DIA])

        while lista_venta1[DIA] == minimo and lista_venta1[DIA] != FIN:
            resultante.write(f"{lista_venta1[DIA]},{lista_venta1[PRODUCTO]},{lista_venta1[VENTAS]}\n")
            lista_venta1 = leer_linea(ventas1)

        while lista_venta2[DIA] == minimo and lista_venta2[DIA] != FIN:
            resultante.write(f"{lista_venta2[DIA]},{lista_venta2[PRODUCTO]},{lista_venta2[VENTAS]}\n")
            lista_venta2 = leer_linea(ventas2)

    ventas1.close()
    ventas2.close()
    resultante.close()

def armado_diccionario():
    diccionario_ventas = {}

    resultante = open("resultante.csv", "r")
    lista_productos = leer_linea(resultante)

    while lista_productos != FIN:

        if lista_productos[PRODUCTO] in diccionario_ventas:
             diccionario_ventas[int(lista_productos[PRODUCTO])] += int(lista_productos[VENTAS])
        else:
            diccionario_ventas[int(lista_productos[PRODUCTO])] = int(lista_productos[VENTAS])

        lista_productos = leer_linea(resultante)
    
    resultante.close()

    return diccionario_ventas

def stock_faltante(reposicion, diccionario_ventas):
    lista_stock = []
    print(reposicion)
    print(diccionario_ventas)
    for cant_productos, elementos in reposicion.items():

        if cant_productos in diccionario_ventas:

            if elementos[STOCK] < diccionario_ventas[cant_productos]:

                lista_stock += [[elementos[NOMBRE], diccionario_ventas[cant_productos] - elementos[STOCK]]]
    
    lista_stock.sort(key=lambda item : item [1], reverse = True)
    return lista_stock

armado_merge()
diccionario_ventas =  armado_diccionario()
reposicion = {30:["Frutas",10], 15:["Leche",4], 25:["Carnes",1]}
lista_stock = stock_faltante(reposicion, diccionario_ventas)
print(lista_stock)