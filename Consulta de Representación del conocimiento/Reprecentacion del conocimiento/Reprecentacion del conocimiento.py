"""En este ejemplo de la Representacion del conocimiento
se usa una clase Animal para retener y posteriormente 
mostrar(usar) la informacion sobre un animal"""
class Animal:
    def __init__(self, especie, edad, nombre):
        self.especie = especie
        self.edad = edad
        self.nombre = nombre
    
    def mostrarInformacion(self):
        print("Especie:", self.especie)
        print("Edad:", self.edad, "años")
        print("Nombre:", self.nombre)

perro = Animal("Perro", 3, "Max")
perro.mostrarInformacion()
