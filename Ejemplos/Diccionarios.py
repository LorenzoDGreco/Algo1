diccionario = {'Racing' : 18, 'VELEZ':11, 'ROSARIO':4}  #Clave : Valor

print(diccionario)

print(diccionario['Racing'])

print(type(diccionario))

print(len(diccionario))

diccionario['FERRO'] = 2
print(diccionario)

del(diccionario["FERRO"])
print(diccionario)

diccionario['Racing'] += 1
print(diccionario)

for clave in diccionario:
    print(clave)

print("-----")

for clave in diccionario.keys():
    print(clave)

lista = diccionario.items()
print(lista)

if 'INDEPENDIENTE' in diccionario:
    print("lo está")
else:
    print("no lo es")



print("-------------")

diccionario = {"El Aleph":"Borges",
                "Sobre Heroes y Tumbas": "E.Sabato", 
                "La Gesta del Marrano" : "M.AGUINIS", 
                "Misteriosa Buenos Aires," : "Mujica Laines", 
                "Fundacion" : "I.Asimov"}
for titulo in diccionario:
    print(diccionario[titulo])

print("------------")

diccionario = {171717:('Lopez',[9,10],('llopez@fi.uba.ar','lopecito77@gmail.com'))}

#print(diccionario[1])
#print(diccionario['171717'])
print(diccionario[171717][2][1])
diccionario[171717][1].append(1) #Se aplica a la lista no al diccionario
print(diccionario[171717][1])

