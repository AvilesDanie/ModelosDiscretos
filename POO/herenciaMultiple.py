class Madre:
    def __init__(self, apellidoMaterno) -> None:
        self.apellidoMaterno = apellidoMaterno


class Padre:
    def __init__(self, apellidoPaterno) -> None:
        self.apellidoPaterno = apellidoPaterno

class Hijo(Madre,Padre):
    def __init__(self, apellidoPaterno, apellidoMaterno) -> None:
        Padre.__init__(self, apellidoPaterno)
        Madre.__init__(self, apellidoMaterno)


Jorge = Hijo("Suarez","Martinez")
print(Jorge.apellidoPaterno)
print(Jorge.apellidoMaterno)