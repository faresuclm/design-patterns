from abc import abstractmethod, ABC

class Bicho:
    def __init__(self, vidas, poder, posicion, modo):
        self.vidas = vidas
        self.poder = poder
        self.posicion = posicion
        self.modo = modo

    def ataca(self):
        self.modo.ataca()

class Modo(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def ataca(self):
        pass

class Agresivo(Modo):

    def __init__(self):
        super().__init__()
        self.poder = 10
        self.vidas = 5

    def ataca(self):
        print("Agresivo: Voy a machacarte")

class Sabio(Modo):

    def __init__(self):
        super().__init__()
        self.poder = 7
        self.vidas = 10

    def ataca(self):
        print("Sabio: Pensemos en la mejor solución")

class Perezoso(Modo):

    def __init__(self):
        super().__init__()
        self.poder = 1
        self.vidas = 5

    def ataca(self):
        print("Perezoso: Buff, qué pereza, mejor me quedo aquí tranquilo")
