class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo.")


class Mamifero(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def alimentar_crias(self):
        print(f"{self.nombre} está alimentando a sus crías.")


class Carnivoro(Mamifero):
    def __init__(self, nombre):
        super().__init__(nombre)

    def cazar(self):
        print(f"{self.nombre} está cazando su presa.")


class Leon(Carnivoro):
    def __init__(self, nombre):
        super().__init__(nombre)

    def rugir(self):
        print(f"{self.nombre} está rugiendo.")


leon = Leon("Raul")
leon.rugir()
leon.cazar()
leon.alimentar_crias()
leon.comer()