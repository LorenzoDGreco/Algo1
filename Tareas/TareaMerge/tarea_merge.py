MAX = "999999"

def leer_info(archivo):
    linea = archivo.readline()
    if linea:
        registro = linea.rstrip("\n").split(",")
    else:
        registro = ["99/99/9999", "999999", "999999","0"]
    return registro

def iteracion_por_archivo(
    archivo, menor, cuenta_ingreso, cuenta_ventas, fecha, codigo_producto, cantidad_ingresos,cantidad_ventas):

    while(codigo_producto == menor and codigo_producto != MAX):
        cuenta_ingreso += int(cantidad_ingresos)
        cuenta_ventas += int(cantidad_ventas)
        fecha, codigo_producto, cantidad_ingresos,cantidad_ventas = leer_info(archivo)

    return cuenta_ingreso, cuenta_ventas, fecha, codigo_producto, cantidad_ingresos,cantidad_ventas

def main():
    tienda1 = open("tienda1.csv", "r")
    tienda2 = open("tienda2.csv", "r")
    tienda3 = open("tienda3.csv", "r")
    archivoescritura = open("archivoescritura.txt", "w")

    tienda1_fecha, tienda1_codigo_producto, tienda1_cantidad_ingresos, tienda1_cantidad_ventas = leer_info(tienda1)
    tienda2_fecha, tienda2_codigo_producto, tienda2_cantidad_ingresos, tienda2_cantidad_ventas = leer_info(tienda2)
    tienda3_fecha, tienda3_codigo_producto, tienda3_cantidad_ingresos, tienda3_cantidad_ventas = leer_info(tienda3)
    tot_ingreso = 0
    tot_ventas = 0

    while tienda1_codigo_producto != MAX or tienda2_codigo_producto != MAX or tienda3_codigo_producto != MAX:
        cuenta_ingreso = 0
        cuenta_ventas = 0
        menor = min(tienda1_codigo_producto, tienda2_codigo_producto, tienda3_codigo_producto)
        

        cuenta_ingreso, cuenta_ventas, tienda1_fecha, tienda1_codigo_producto, tienda1_cantidad_ingresos,tienda1_cantidad_ventas = iteracion_por_archivo(
            tienda1, menor, cuenta_ingreso, cuenta_ventas, tienda1_fecha, tienda1_codigo_producto, tienda1_cantidad_ingresos,tienda1_cantidad_ventas)

        cuenta_ingreso, cuenta_ventas, tienda2_fecha, tienda2_codigo_producto, tienda2_cantidad_ingresos,tienda2_cantidad_ventas = iteracion_por_archivo(
            tienda2, menor, cuenta_ingreso, cuenta_ventas, tienda2_fecha, tienda2_codigo_producto, tienda2_cantidad_ingresos,tienda2_cantidad_ventas)

        cuenta_ingreso, cuenta_ventas, tienda3_fecha, tienda3_codigo_producto, tienda3_cantidad_ingresos,tienda3_cantidad_ventas = iteracion_por_archivo(
            tienda3, menor, cuenta_ingreso, cuenta_ventas, tienda3_fecha, tienda3_codigo_producto, tienda3_cantidad_ingresos,tienda3_cantidad_ventas)

        archivoescritura.write(f"El producto: {menor} ha generado {cuenta_ingreso} ingresos con {cuenta_ventas} ventas\n")
        tot_ingreso += cuenta_ingreso
        tot_ventas += cuenta_ventas

    archivoescritura.write(f"El final de todos los productos ha generado {tot_ingreso} ingresos con {tot_ventas} ventas")
    tienda1.close()
    tienda2.close()
    tienda3.close()
    archivoescritura.close()

main()