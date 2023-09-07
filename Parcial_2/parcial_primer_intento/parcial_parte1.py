FIN = "XXXXX"
DIA = 0
PRODUCTO = 1
VENTAS = 2

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

armado_merge()

