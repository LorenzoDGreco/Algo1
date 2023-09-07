def Factorizar(numero):
    """
    Recibe el valor ingresado por el usuario
    y devuelve el valor factorizado
    para imprimir en pantalla

    Siendo el Dominio de n! = { 1        , n=0 o n=1  
                              { 1x2x3...n, n>=2
    """
    
    if(numero >= 0):
        numFactorizado = 1
        for bucle in range (1,numero+1):
            numFactorizado = numFactorizado * bucle
    else:
        numFactorizado = 0
    return numFactorizado

#----------- Main ----------------#

numero = int(input("Ingrese un numero para factorizar: "))

print("El resultado del factorizado es: ", Factorizar(numero))
