from bicho import Bicho
from elemento_mapa import *
from pared import *
from puerta import Puerta, PuertaBlindada
from contenedor import Cuadrado
from orientacion import *
from habitacion import Habitacion
from laberinto import Laberinto

class Creator:
    def crear_habitacion(self, num) -> Habitacion:
        habitacion = Habitacion(num)
        habitacion.forma = self.crear_forma()
        pared_norte = self.fabricar_pared()
        habitacion.ponerElementoEnOrientacion(pared_norte, Norte())
        pared_sur = self.crear_pared()
        habitacion.ponerElementoEnOrientacion(pared_sur, Sur())
        pared_este = self.crear_pared()
        habitacion.ponerElementoEnOrientacion(pared_este, Este())
        pared_oeste = self.crear_pared()
        habitacion.ponerElementoEnOrientacion(pared_oeste, Oeste())
        return habitacion
    

    def crear_forma(self):
         forma=Cuadrado()
         forma.agregarOrientacion(self.fabricarNorte())
         forma.agregarOrientacion(self.fabricarSur())
         forma.agregarOrientacion(self.fabricarEste())
         forma.agregarOrientacion(self.fabricarOeste())
         return forma
    
    def fabricarNorte(self):
        return Norte()
    
    def fabricarSur(self):
        return Sur()
    
    def fabricarEste(self):
        return Este()
    
    def fabricarOeste(self):
        return Oeste()

    def fabricar_laberinto(self) -> Laberinto:
        return Laberinto()

    def fabricar_pared(self)-> Pared:
        return Pared()

    def fabricar_puerta(self, lado1, lado2)-> Puerta:
        return Puerta(lado1, lado2)
    
    def crear_bomba(self,pared:ParedBomba) -> ParedBomba:
        creator = CreatorB()
        return creator.fabricar_pared()
    
    def crear_bicho(self,vidas,poder,posicion,modo):
        bicho=Bicho();
        bicho.vidas=vidas
        bicho.poder=poder
        bicho.posicion=posicion
        bicho.modo=modo
        return bicho

class CreatorB(Creator):

    def fabricar_pared(self)-> ParedBomba:
        return ParedBomba()

class CreatorBlind(Creator):

    def fabricar_puerta(self, lado1, lado2)-> PuertaBlindada:
        return PuertaBlindada(lado1, lado2)
