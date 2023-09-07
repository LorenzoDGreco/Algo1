MAXIMOS_INTENTOS_LOGIN = 3

def continuar_intento_login(usuario_esta_logueado_correctamente, intentos):
    '''
    Retorna True si el login se produjo de forma exitosa o si se alcanzaron la cantidad           máxima de intentos
    '''
    while not usuario_esta_logueado_correctamente and intentos < MAXIMOS_INTENTOS_LOGIN:
        usuario = input("Por favor ingrese un usuario: ")
        es_usuario_valido(usuario)

        print("Ahora ingrese la contraseña asociada al usuario a este usuario")
        contrasenia = input("Por favor ingrese una contraseña: ")
        usuario_esta_logueado_correctamente = es_login_valido(usuario, contrasenia)

        intentos += 1
        intentos_restantes = MAXIMOS_INTENTOS_LOGIN - intentos

        
    
        informar_intentos_restantes(intentos_restantes,usuario_esta_logueado_correctamente)
    
        saludar_usuario(usuario_esta_logueado_correctamente)


        
    return intentos_restantes

def es_usuario_valido(usuario):
    '''
    Verifica que el nombre de usuario ingresado por el usuario sea válido
    '''
    while not(usuario == "Juan" or usuario == "Franco"):
        print("Usuario inválido!")
        usuario = input("Por favor ingrese un usuario: ")
    print("Usuario válido!")
    return usuario

def es_login_valido(usuario, contrasenia):
    '''
    Retorna True si un par usuario contraseña es válido, False en caso contrario
    '''
    if usuario == "Juan":
        if contrasenia == "panconqueso":
            print("Bienvenido al sistema", usuario, "!")
            esta_logueado_correctamente = True
        else:
            print("Contraseña inválida!")
            esta_logueado_correctamente = False
    else:
        if contrasenia == "eladera123":
            print("Bienvenido al sistema", usuario, "!")
            esta_logueado_correctamente = True
        else:
            print("Contraseña inválida!")
            esta_logueado_correctamente = False
            
    return esta_logueado_correctamente

def informar_intentos_restantes(intentos_restantes, usuario_esta_logueado_correctamente):
    '''
    Informa al usuario cuantos intentos restantes de login le quedan, siempre comparando con       la cantidad máxima de intentos. Retorna el mensaje correspondiente.
    '''
    if not usuario_esta_logueado_correctamente:
        if intentos_restantes > 0:
            print("Vuelva a intentarlo, le quedan", intentos_restantes, "intentos")
        else:
            print("Ohno, no le quedan mas intentos de login!")
    return intentos_restantes

def saludar_usuario(usuario_esta_logueado_correctamente):
    '''
    Saluda al usuario de distintas formas, en base a si un login se produció de forma correcta o no. Retorna el mensaje correspondiente.
    '''
    if usuario_esta_logueado_correctamente:
        print("Disfrute su estadia!")
    else:
        print("Suerte la próxima!")
    return usuario_esta_logueado_correctamente

def login():
    print("¡Bienvenido al sistema de login!")
    usuario_esta_logueado_correctamente = False
    intentos_login = 0

    continuar_intento_login(usuario_esta_logueado_correctamente, intentos_login)

    


login()
