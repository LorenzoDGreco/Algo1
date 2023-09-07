class Persona:
    def saludarAmigo(self, amigo):
        print("Hola" + amigo + "! Como va?")

nicolas = Persona()
nicolas.saludarAmigo("Perdro")

#---------------------------------------------------------

class Persona2:
    def __init__(self, nombre, colorDePelo):
        self.nombre = nombre
        self.colorDePelo = colorDePelo

    def decirNombre(self):
        print("Me llamo " + self.nombre + " " + self.colorDePelo )

nicolas = Persona2("Nicolas", "Castaño")
joaquin = Persona2 ("Joaquin", "Rojo")

nicolas.decirNombre()
joaquin.decirNombre()

#-----------------------------------------------------------

