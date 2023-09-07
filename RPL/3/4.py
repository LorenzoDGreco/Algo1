def es_capicua_2(palabra):
    es_capicua = False
    incrementador = 0
    for caracter in palabra:
        for caracter_inverso in range(len(palabra)-1, -1, -1):
            if(caracter == palabra[caracter_inverso]):
                incrementador += 1
                
    if(((len(palabra)*2)-1) == (incrementador)):
        es_capicua = True
        
    return es_capicua

def es_capicua_3(palabra):
    es_capicua = False
    incrementador = 0
    for caracter in palabra:
        for caracter_inverso in range(len(palabra)-1, 0, -1):
            if(caracter == palabra[caracter_inverso]):
                incrementador += 1
                break
                
    if(len(palabra) == (incrementador)):
        es_capicua = True
        
    return es_capicua


def es_capicua(palabra):
    return palabra == palabra[::-1]


print(es_capicua("neuquen"))
print(es_capicua("alfonsin"))
print(es_capicua("menem"))
print(es_capicua("alfonsin"))
