#diccionario = {}

#diccionario.keys()
#diccionario.values()
#diccionario.items()

#for i in range(1,6):
#    diccionario(i) = "Es un buen tipo :D"
#print(diccionario)

diccinario_canciones = {"artista":{"nombre":"Juan","Album":"La Granja", "Cancion":"El cantar del pollo","Duracion":"4:31", "Anio":"1993"}}

#print(diccinario_canciones)
#for valores in diccinario_canciones.values():
#    if "Juan" in valores.values():
#        print(valores["nombre"])

for artista in diccinario_canciones:
    if "Juan" in diccinario_canciones[artista].values():
        print(True)

