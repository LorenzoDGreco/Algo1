def elegir_pelicula2(actores, puntajes, actores_preferidos):
    ver_pelicula = False
    promedio = sum(puntajes)/len(puntajes)
    if promedio >= 6:
        for actores_unitarios in actores:
            for actores_pref_unitarios in actores_preferidos:
                if(actores_pref_unitarios == actores_unitarios):
                    ver_pelicula = True
    return ver_pelicula

def elegir_pelicula(actores, puntajes, actores_preferidos):
    ver_pelicula = False
    promedio = sum(puntajes)/len(puntajes)
    if promedio >= 6:
        i=0
        while len(actores)>i and not ver_pelicula:
            if(actores[i] in actores_preferidos):
                ver_pelicula = True
            i += 1
    return ver_pelicula


actores = ["Aleandro", "Villamil", "Darin", "Francella"]
actores2 = ["De niro", "Deep", "Blanchett", "Colman"]
puntajes = [4,5,7,4,10] 
puntajes2= [4,5,7,4,9,6]
actores_preferidos = ["Villamil", "DiCaprio"]


print(elegir_pelicula(actores, puntajes, actores2))
print(elegir_pelicula(actores2, puntajes2, actores_preferidos))
print(elegir_pelicula(actores, puntajes2, actores_preferidos))
print(elegir_pelicula(actores, puntajes, actores_preferidos))
