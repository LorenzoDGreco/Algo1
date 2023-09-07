PERSONAS = 0
EMPLEADOS = 1
LOCALIDAD = 0
DESOCUPACION = 1

def ingresar_datos():
    bucle = ""
    desocupacion = 0
    diccionario =  {}
    lista = []
    while bucle != "n":
        localidad = input("Ingrese localidad: ")
        personas =  int(input("Ingrese la cantidad de personas que pueden trabajar: "))
        empleados =  int(input("Ingrese la cantidad de empleados: "))
        if(localidad in diccionario):
            lista.extend([personas, empleados])
            for i in range(0,2):
                diccionario[localidad][i] += lista[i]
        else:
            lista.extend([personas, empleados])
            diccionario[localidad] = lista
        lista = []
        bucle = input("Desea seguir ingresando?(s/n): ")

    return diccionario

def ordenar_valores(diccionario):
    for clave, valor in diccionario.items():
        print("En la localidad de " + clave + " hay " + str(valor[PERSONAS]) + " personas en edad laboral y " + str(valor[EMPLEADOS]) + " trabajando.")

    desocupacion = 0
    lista = []
    i=0
    for clave, valor in diccionario.items():
        desocupacion = (1 - valor[EMPLEADOS] / valor[PERSONAS]) * 100
        lista.extend([[clave,desocupacion]])
        lista.sort(key = lambda item:item[1],reverse = True)
    print(lista)
    for elemento in lista:
        print("La tasa de desocupacion en " + elemento[LOCALIDAD] + " es " + str(round(elemento[DESOCUPACION],2)) + "%.")
        i+=1
    return 0

diccionario = {}
diccionario = ingresar_datos()
ordenar_valores(diccionario)