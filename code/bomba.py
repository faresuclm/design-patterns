from abc import abstractmethod, ABC
from decorator import Decorator

### BOMBAS ########
class Bomba(Decorator):
    def __init__(self, em, tipo):
        super().__init__(em)
        self.activa = False
        self.tipo_bomba = tipo

    def esBomba(self):
        return True

class TipoBomba(Bomba, ABC):

    @abstractmethod
    def explotar(self):
        pass

class Mina(TipoBomba):

    def explotar(self):
        super().explotar()
        print("Lo siento has pisado una mina")
        print("💣💣💣💣💣")

class Broma(TipoBomba):

    def explotar(self):
        super().explotar()
        print("Explosión inminente")
        print("😂😂😂😂😂, Era broma")

class Destructiva(TipoBomba):

    def explotar(self):
        super().explotar()
        print("Bomba de destrucción masiva activada")
        print("BOOOOOOOOOOOOOOOOMMMMM")
