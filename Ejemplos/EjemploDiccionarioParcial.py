def tiene_mas_partidos(equipos):
    partida_tot = 0
    for equipo, partidas in equipos.items():
        if sum(partidas) > partida_tot or partida_tot == 0:
            partida_tot = sum(partidas)
            lista = [equipo, partida_tot]
    print("El equipo " + lista[0] + " es el que tiene mayor numero de partidas con: " + str(lista[1]))

def equipos_listados(equipos):
    lista_ordenada = []
    for equipo, partidas in equipos.items():
        lista_ordenada += [[equipo, partidas[0] * 3 + partidas[1]]]

    lista_ordenada.sort(key = lambda item: item[1], reverse = True)

    for elemento in lista_ordenada:
        print("El equipo " + elemento[0] +  " tiene " + str(elemento[1]) + " puntos")


diccionario = {"River": [3,1,0], "Boca": [0,8,0], "Platense": [2,1]}
tiene_mas_partidos(diccionario)
equipos_listados(diccionario)