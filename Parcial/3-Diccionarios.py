def votaciones(lista_votos):
    diccionario_votos = {}
    for elementos in lista_votos:
        if elementos[0] in diccionario_votos:
            diccionario_votos[elementos[0]] += elementos[1] + elementos[2]
        else:
            diccionario_votos[elementos[0]] = elementos[1] + elementos[2]
    return diccionario_votos


def ordenar_votos(diccionario_votos):
    lista_ordenada = diccionario_votos.items()
    lista_ordenada = sorted(
        lista_ordenada, key=lambda item: item[1], reverse=True)

    for elementos in lista_ordenada:
        print("El partido " + elementos[0] +
              " ha sacado " + str(elementos[1]) + " votos")


diccionario = votaciones([["PP", 19, 35], ["PSOE", 20, 30], [
                         "VOX", 15, 15], ["PP", 0, 15]])
ordenar_votos(diccionario)
