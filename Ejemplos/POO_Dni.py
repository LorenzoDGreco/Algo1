class Persona:
    ultimo_dni = 0

    def __init__(self):
        self.dni = self.ultimo_dni + 1
        # self.ultimo_dni = self.ultimo_dni + 1 está mal!!, genera nuevas variables
        Persona.aumentar_ultimo_dni()

    @classmethod
    def aumentar_ultimo_dni(cls):
        cls.ultimo_dni = cls.ultimo_dni + 1

    def mostrar_dni(self):
        print(self.dni)

    def mostrar_ultimo_dni(self):
        print(self.ultimo_dni)  

def main():
    nicolas = Persona()
    joaquin = Persona()
    julia = Persona()

    print("Mi nombre es Nicolas y mi dni es ", end = "")
    nicolas.mostrar_dni()

    print("Mi nombre es Joaquin y mi dni es ", end = "")
    joaquin.mostrar_dni()

    print("Mi nombre es Julia y mi dni es ", end = "")
    julia.mostrar_dni()

main()