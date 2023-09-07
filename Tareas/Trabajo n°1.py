# Trabajo N°1

def Funcion_Mes (numero_mes):

    if(numero_mes == 1):
        mes = "Enero"
    elif(numero_mes == 2):
        mes = "Febrero"
    elif(numero_mes == 3):
        mes = "Marzo"
    elif(numero_mes == 4):
        mes = "Abril"
    elif(numero_mes == 5):
        mes = "Mayo"
    elif(numero_mes == 6):
        mes = "Junio"
    elif(numero_mes == 7):
        mes = "Julio"
    elif(numero_mes == 8):
        mes = "Agosto"
    elif(numero_mes == 9):
        mes = "Septiembre"
    elif(numero_mes == 10):
        mes = "Octubre"
    elif(numero_mes == 11):
        mes = "Noviembre"
    elif(numero_mes == 12):
        mes = "Diciembre"
    else:
        mes = "Mes Ingresado: Invalido"

    return mes

#---------- Programa Main ---------------------------------------

numero = int(input("Ingrese el numero del mes que se requiera y se le dirá el nombre del mes: "))

print(Funcion_Mes(numero))
