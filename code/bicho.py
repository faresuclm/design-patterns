from abc import abstractmethod, ABC
from agresivo import Agresivo
from perezoso import Perezoso
from sabio import Sabio

class Bicho:
    def __init__(self, vidas, poder, posicion, modo):
        self.vidas = vidas
        self.poder = poder
        self.posicion = posicion
        self.modo = modo
        self.poder = None
        self.vidas = None
        self.posicion = None

    def ataca(self):
        self.modo.ataca()

    def actua(self):
        while self.estaVivo():
            self.modo.actuar(self)

    def iniAgresivo(self):
        self.modo = Agresivo()
        self.poder = 10
        self.vidas = 5

    def iniPerezoso(self):
        self.poder = 1
        self.vidas = 5

    def iniSabio(self):
        self.poder = 5
        self.vidas = 10

    def estaVivo(self):
        return self.vidas > 0

    def __str__(self):
        return "Soy un bicho"+self.modo.__str__()