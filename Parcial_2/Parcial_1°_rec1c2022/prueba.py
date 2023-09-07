FIN = "XXXXXX"

def leer_linea(archivo):
    linea = archivo.readline()
    return linea.rstrip("\n").split(",") if linea else FIN

def apareo():

    stock = open("stock.csv", "r")
    actualizacion = open("actualizacion.csv", "r")
    errores = open("errores.csv", "w")
    stock_nuevo = open("stock_nuevo.csv","w")

    lista_stock = leer_linea(stock)
    lista_actualizacion = leer_linea(actualizacion)
    diccionario_novedades = {}

    while lista_stock != FIN and lista_actualizacion != FIN:
        cantidad_actual = 0
        if int(lista_stock[0]) == int(lista_actualizacion[0]):
            cantidad_actual = int(lista_stock[1]) + (int(lista_actualizacion[1]) - int(lista_actualizacion[2]))
            
            if cantidad_actual < 0:
                errores.write(f"{lista_actualizacion[0]},{cantidad_actual}\n")
            else:
                stock_nuevo.write(f"{lista_actualizacion[0]},{cantidad_actual}\n")

            lista_actualizacion = leer_linea(actualizacion)
            lista_stock = leer_linea(stock)
        
        elif int(lista_stock[0]) < int(lista_actualizacion[0]):
            stock_nuevo.write(f"{lista_stock[0]},{lista_stock[1]}\n")
            lista_stock = leer_linea(stock)

        elif int(lista_stock[0]) > int(lista_actualizacion[0]):
            cantidad_actual = int(lista_actualizacion[1]) - int(lista_actualizacion[2])   

            if cantidad_actual < 0:
                errores.write(f"{lista_actualizacion[0]},{cantidad_actual}\n")
            else:
                stock_nuevo.write(f"{lista_actualizacion[0]},{cantidad_actual}\n")
                diccionario_novedades[int(lista_actualizacion[0])] = int(lista_actualizacion[1]) / int(lista_actualizacion[2])

            lista_actualizacion = leer_linea(actualizacion)


    while lista_stock != FIN:
        stock_nuevo.write(f"{lista_stock[0]},{lista_stock[1]}\n")
        lista_stock = leer_linea(stock)


    while lista_actualizacion != FIN:
        stock_nuevo.write(f"{lista_stock[0]},{lista_stock[1]}\n")
        lista_actualizacion = leer_linea(actualizacion)

    stock.close()
    actualizacion.close()
    errores.close()
    stock_nuevo.close()
    
    return diccionario_novedades

def ordenar_mostrar(diccionario_novedades):

    lista_novedades_ordenada = list(diccionario_novedades.items())

    lista_novedades_ordenada.sort(key = lambda item: item [1], reverse = True)

    print(lista_novedades_ordenada)


diccionario_novedades = apareo()

ordenar_mostrar(diccionario_novedades)