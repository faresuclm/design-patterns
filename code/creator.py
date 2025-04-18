from code.elemento_mapa import *
from pared import *
from puerta import Puerta, PuertaBlindada

class Creator:
    def crear_habitacion(self, num) -> Habitacion:
        habitacion = Habitacion(num)
        habitacion.norte = self.fabricar_pared()
        habitacion.sur = self.fabricar_pared()
        habitacion.este = self.fabricar_pared()
        habitacion.oeste = self.fabricar_pared()
        return habitacion

    def fabricar_laberinto(self) -> Laberinto:
        return Laberinto()

    def fabricar_pared(self)-> Pared:
        return Pared()

    def fabricar_puerta(self, lado1, lado2)-> Puerta:
        return Puerta(lado1, lado2)
    
    def crear_bomba(self,pared:ParedBomba) -> ParedBomba:
        creator = CreatorB()
        return creator.fabricar_pared()

class CreatorB(Creator):

    def fabricar_pared(self)-> ParedBomba:
        return ParedBomba()

class CreatorBlind(Creator):

    def fabricar_puerta(self, lado1, lado2)-> PuertaBlindada:
        return PuertaBlindada(lado1, lado2)
