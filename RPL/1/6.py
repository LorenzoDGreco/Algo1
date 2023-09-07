local = input("Ingrese equipo local: ")
goles_local = input("Ingrese goles equipo local: ")

visitante = input("Ingrese equipo visitante: ")
goles_visitante = input("Ingrese goles equipo visitante: ")

if(goles_local > goles_visitante):
    print(local)
elif(goles_visitante < goles_local):
    print(visitante)
else:
    print("Empate")
