class Padre:
    def __init__ (self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludar(self):
        return f"{self.nombre} es de apellido {self.apellido}."
    
class Hijo(Padre):
    def __init__(self,nombre,apellido):
        super().__init__(nombre,apellido)

Jorge = Hijo("Juan","Gonzaga")
print(Jorge.apellido)
print(Jorge.saludar())


class Yo:
    def __init__ (self,nombre,apellido,carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.carrera = carrera

    def habilidad(self):
        return f"Soy {self.nombre} {self.apellido} de la carrera de {self.carrera} y mi habilidad es "


yo = Yo("Daniel","Aviles","Software")
print(yo.habilidad())