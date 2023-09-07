def letra_repetida(palabra):
    diccionario = {}
    for caracter in palabra:
        if caracter in diccionario:
            diccionario[caracter] += 1
        else:
            diccionario[caracter] = 1
    return diccionario

print(letra_repetida("analisis"))


diccionario = {1:[2,300], 2:[5000,3], 5:[60,400]}
total = 0
for clave in diccionario:
    total += diccionario[clave][0] * diccionario[clave][1]
print(total)

total2 = 2*300 + 5000*3 + 60*400
print(total2)