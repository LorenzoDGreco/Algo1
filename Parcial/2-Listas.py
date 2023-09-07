MAX_CUOTA = 5000


def asociarse(actividades, actividades_deseadas, cuotas):
    asociarse = False
    contador_actividades = 0
    if cuotas <= MAX_CUOTA:
        i = 0
        while len(actividades) > i and contador_actividades < 2:
            if actividades[i] in actividades_deseadas:
                contador_actividades += 1
            i += 1
        if contador_actividades >= 2:
            asociarse = True
    return asociarse


lista_1 = ["natacion", "gimnasio", "voley", "futbol"]
lista_2 = ["natacion", "voley", "gimnasio"]
lista_3 = ["natacion", "futbol", "karate"]

print(asociarse(lista_1, lista_2, 5000))
print(asociarse(lista_1, lista_3, 5000))
print(asociarse(lista_2, lista_3, 100))
