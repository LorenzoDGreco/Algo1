class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        self.elementos.append(elemento)

    def pop(self):
        return self.elementos.pop()


class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, elemento):
        self.elementos.append(elemento)

    def desencolar(self):
        return self.elementos.pop(0)

    def mostrarCola(self):
        print(self.elementos)


class PrioridadError(Exception):
    pass


class ColaDePrioridad:
    MAX_PRIORIDAD = 3

    def __init__(self):
        self.elementos = [Cola() for _ in range(0, self.MAX_PRIORIDAD)]

    def encolar(self, elemento, prioridad=1):
        if prioridad <=0:
            raise PrioridadError("No se puede ingresar una prioridad menor a 1")
        if prioridad > self.MAX_PRIORIDAD:
            raise PrioridadError(f"no se puede ingresar una prioridad mayor a {self.MAX_PRIORIDAD}")
        self.elementos[prioridad - 1].encolar(elemento)

    def mostrarColas(self):
        for cola in self.elementos:
            cola.mostrarCola()

    def desencolar(self):
        elementoDesencolado = False
        prioridad = 0
        while not elementoDesencolado:
            try:
                elemento = self.elementos[prioridad].desencolar()
                elementoDesencolado = True
            except IndexError as e:
                prioridad = prioridad + 1
                if prioridad == self.MAX_PRIORIDAD:
                    raise e

        return elemento




def main():
    pila = Pila()
    cola = Cola()
    colaDePrioridad = ColaDePrioridad()

    print("PILA")
    print("Se ingresan los valores 1, 2, 3. En ese orden")

    pila.push(1)
    pila.push(2)
    pila.push(3)

    print("Se sacan los valores uno a uno")

    print(pila.pop())
    print(pila.pop())
    print(pila.pop())

    print("----------")
    print("COLA")
    print("Se ingresan los valores 4, 5, 6. En ese orden")

    cola.encolar(4)
    cola.encolar(5)
    cola.encolar(6)

    print("Se sacan los valores uno a uno")

    print(cola.desencolar())
    print(cola.desencolar())
    print(cola.desencolar())

    print("----------")
    print("COLA DE PRIORIDAD")
    print("Se ingresan los valores 4, 5, 6, 7, 8, 9. En ese orden pero con distintas prioridades")

    colaDePrioridad.encolar(4, 2)
    colaDePrioridad.encolar(5, 3)
    colaDePrioridad.encolar(6)
    colaDePrioridad.encolar(7)
    colaDePrioridad.encolar(8, 2)
    colaDePrioridad.encolar(9, 2)

    print("Se sacan los valores uno a uno")

    colaDePrioridad.mostrarColas()

    print(colaDePrioridad.desencolar())
    print(colaDePrioridad.desencolar())
    print(colaDePrioridad.desencolar())
    print(colaDePrioridad.desencolar())
    print(colaDePrioridad.desencolar())
    print(colaDePrioridad.desencolar())


main()