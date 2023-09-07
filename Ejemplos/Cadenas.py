linea = 'Ella dijo: "REKATATHE LORO"'
print(linea)

linea = """Ella dijo: rekatate loro"""
print (linea)

linea = ("Texto 1" "Texto 2" "Texto 3")
print(linea)

linea = "Algoritmo"
#print(linea[1]) #no existe esto pero algo así es
print(linea[0:4]) #me corta la linea de 0 a 4

print(len(linea)) #me dice el total de la cadena (SIN CONTAR EL 0)

print(linea.upper()) # ME LO DA TODO EN MAYUSCULAS AAAAA

print(linea.count("o")) # Devuelve la cantidad de letras que haya sido marcada

print(linea.index("A")) #Nos devuelve la posicion de A en la cadena, si no tiene da ERROR

print(linea.find("ori")) #nos devuelve la posicion de "ori" sino da -1

print(linea.isalpha()) # si solo tiene letras devuelve True sino False

print(linea.isnumeric()) #si solo tiene numeros da True sino False

print(linea.isalnum()) #si tiene numeros y/o letras da True sino False



print("------------------------------")



linea = "que lee boludo?"

#for i in linea:
#    print(i)

#for i in range(len(linea)):
#    print(linea[i])


for i in range(0,len(linea),2):
    print(linea[i])

    
print("------------------------------")


i=0
while (i < len(linea) and linea[i]!="o"):
    print(linea[i])
    i+=1


print("------------------------------")



