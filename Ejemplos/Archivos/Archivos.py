# csv caracter separados por comas
# bin archivo binario

#r = Read
#r+ = Read & Write no se borra
#w = Write BORRA TODo ANTES DE ESCRIBIR
#a = Append agrega al final
#b = lo lee en Binario

#SI EL ARCHIVO NO ENTRA EN MEMORIA USAR readline()
#Si se tiene un archivo LEER SOLO UNA VEZ

archivo = open("hola.txt", "r")

linea = archivo.read()
print(linea)

print("----")

linea = archivo.readlines()
print(linea)

print("----")

linea = archivo.readline() #Siempre usar este para no cargar toda la memoria
print(linea)

print("----")

# linea = archivo.read(bytes)
# print(linea)

#Indica la posición del puntero en el archivo en bytes
print(archivo.tell()) #Muestra la posicion del puntero


print("----")

# Sirve para mover el puntero en el archivo 
# una cantidad de bytes fija hacia adelante o hacia atrás
print(archivo.seek(0)) #seek(CUANTOS, DESDE) 0:INICIO 1:ACTUAL 2:FINAL, no utilizar porque eso sería volver a leer el archivo

print("----")

for linea in archivo:
    print(linea)

# while linea != "":
#     print(linea, end = "")
#     linea = archivo.readline()

archivo.close()


try:
	archivo = open("hola3.csv")
except FileNotFoundError:
	archivo = open("hola3.csv", "w")
	archivo.close()
	archivo = open("hola3.csv", "r+")


archivo.write("hola")

linea = archivo.readlines()
print(linea)

archivo.close()