# def ingresar_valores():
#     equipo = ""
#     lista = []
#     diccionario = {}
#     while equipo != "n":
#         equipo = input("Ingrese el nombre del equipo: ")
#         lista.append(int(input("Ingrese la cantidad de partidos ganados: ")))
#         lista.append(int(input("Ingrese la cantidad de partidos empatados: ")))
#         lista.append(int(input("Ingrese la cantidad de partidos perdidos: ")))
#         lista.append(int(input("Ingrese la cantidad de goles realizados: ")))
#         lista.append(int(input("Ingrese la cantidad de goles recibidos: ")))
        
#         if equipo in diccionario:
#             for i in range(0,5):
#                 diccionario[equipo][i] += lista[i]
#         else:
#             diccionario[equipo] = lista

#         lista = []

#         equipo = input("Desea ingresar otro usuario? (s/n): ")
#     return diccionario

def comprobaciones(diccionario):
    equipo_ganador = 0
    equipo_desciende = 99999
    equipo_goleador = 0
    contador_puntos = 0
    lista = [[0,0],[0,0],[0,0],[0,0]] #0:ganador 1:desciende 2:empate 3:goleador

    for clave in diccionario:
        for i in range(0,4):
            if i == 0:
                contador_puntos += diccionario[clave][i] * 3
            elif i == 1:
                contador_puntos += diccionario[clave][i]
                if lista[2][1] < diccionario[clave][i]:
                    lista[2] = clave,diccionario[clave][i]
            elif i == 3:
                if diccionario[clave][i+1] == 0:
                    diccionario[clave][i+1] = 1
                equipo_goleador = diccionario[clave][i] / diccionario[clave][i+1]
                if lista[3][1] < equipo_goleador:
                    lista[3] = clave,equipo_goleador

        if equipo_ganador < contador_puntos:
            equipo_ganador = contador_puntos
            lista[0] = clave,equipo_ganador
            
        if equipo_desciende > contador_puntos:
            equipo_desciende = contador_puntos
            lista[1] = clave,equipo_desciende

        contador_puntos = 0
    return lista

def main():
    lista = comprobaciones({"Racing":[4,5,0,15,8], "Central":[7,1,0,8,6], "Gimnasia LP":[0,2,0,4,4], "San Lorenzo":[1,8,1,1,2]})
    
    print("El equipo campeon es " + lista[0][0] + " con " + str(lista[0][1]) + " puntos.")
    print("El equipo que desciende es " + lista[1][0] + " con " + str(lista[1][1]) + " puntos.")
    print("El equipo que mas partidos empato es " + lista[2][0] + " con " + str(lista[2][1]) + " partidos.")
    print("El equipo con mejor proporcion goleadora es " + lista[3][0] + " con " + str(lista[3][1]) + ".")

    return

main()