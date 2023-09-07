lista = [4,6,2]


a = int(input("Ingrese un entero: "))
b = int(input("Ingrese otro entero: "))
try:
    resultado = a/b
    print("La division es: ", resultado)
    print(lista[2])
except ZeroDivisionError:
    print("Se produjo un error por división por cero")
except IndexError:
    print("Se produjo un error por indice fuera de rango")
except NameError:
    print("Hay una variable que no está definida")
except Exception:
    print("ALTO TODO! ALGO PASO Y NO TENGO NI IDEA")
finally:
    print("Esto siempre se ejecuta :)")
print("Termino el programa")



def f(x,y):
    if(x <= 0 or y <= 0):
        raise ValueError("Alguna variable es negativa")
    return(x / y)

try:
    print(f(5,-3))
except Exception as e:
    print("Error: ", e)