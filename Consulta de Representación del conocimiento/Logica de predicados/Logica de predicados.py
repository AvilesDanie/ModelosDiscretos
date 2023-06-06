"""En este ejemplo de logica de predicados se
    tiene una clase perro con la funcion ladrar
    y con la funcion todosLosPerrosLadran se 
    busca verificar la premisa"""
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def ladrar(self):
        print(self.nombre + " está ladrando.")
        return True

def todosLosPerrosLadran(perros):
    for perro in perros:
        if not perro.ladrar():
            return False
    return True

listaPerros = [Perro("Max"), Perro("Bella"), Perro("Charlie")]

if todosLosPerrosLadran(listaPerros):
    print("Todos los perros ladran.")
else:
    print("No todos los perros ladran.")
