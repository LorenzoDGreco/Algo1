def calculador_promedio(suma_votos, cantidad_votos):
    promedio = suma_votos/cantidad_votos
    return promedio


def generador_diccionario(lista):
    diccionario = {}
    participante = 0
    votos = 1
    for sublista in lista:
        if sublista[participante] not in diccionario:
            diccionario[sublista[participante]] = [sublista[votos], 1]
        else:
            diccionario[sublista[participante]] += [sublista[votos], 1]
    for persona, valores in diccionario.items():
        promedio = calculador_promedio(valores[0], valores[1])
        diccionario[persona] += [promedio]
    return diccionario


def main():
    lista = [["Luisa", 4], ["Mariano", 10], ["Luisa", 5],
             ["Valen", 8], ["Alan", 2], ["Cande", 0]]
    diccionario = generador_diccionario(lista)
    participante = 0
    valor = 1
    promedio = 2
    lista_ordenada = sorted(
        diccionario.items(), key=lambda item: item[valor][promedio], reverse=True)
    for concursante in lista_ordenada:
        print(concursante[participante], "   ", concursante[valor][promedio])


main()
