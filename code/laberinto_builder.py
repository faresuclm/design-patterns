from laberinto import Laberinto
from juego import Juego
from puerta import Puerta
from orientacion import Norte
from orientacion import Sur
from orientacion import Este
from orientacion import Oeste 
from habitacion import Habitacion
from pared import Pared 
from bicho import Bicho
from agresivo import Agresivo
from perezoso import Perezoso
from sabio import Sabio

class LaberintoBuilder:
    def __init__(self):
        self.laberinto = None
        self.juego=None

    def fabricarJuego(self):
        self.juego=Juego()
        self.juego.laberinto=self.laberinto

    def fabricarLaberinto(self):
        self.laberinto = Laberinto()

    def fabricarHabitacion(self, num):
        hab=Habitacion(num)	
        hab.agregarOrientacion(self.fabricarNorte())
        hab.agregarOrientacion(self.fabricarSur())
        hab.agregarOrientacion(self.fabricarEste())
        hab.agregarOrientacion(self.fabricarOeste())
        for orientacion in hab.orientaciones:
            hab.ponerElementoEnOrientacion(self.fabricarPared(),orientacion)
        self.laberinto.agregar_habitacion(hab)
        return hab

    def fabricarPared(self):
        return Pared()

    def fabricarPuerta(self, lado1,o1,lado2,o2):
        hab1=self.laberinto.obtenerHabitacion(lado1)
        hab2=self.laberinto.obtenerHabitacion(lado2)
        puerta=Puerta(hab1,hab2)
        objOr1=self.obtenerObjeto(o1)
        objOr2=self.obtenerObjeto(o2)
        hab1.ponerElementoEnOrientacion(puerta,objOr1)
        hab2.ponerElementoEnOrientacion(puerta,objOr2)
    
    def obtenerObjeto(self,cadena):
        obj=None
        match cadena:
            case 'Norte':
                obj=self.fabricarNorte()
            case 'Sur':
                obj=self.fabricarSur()
            case 'Este':
                obj=self.fabricarEste()
            case 'Oeste':
                obj=self.fabricarOeste()
        return obj
     
    def fabricarNorte(self):
        return Norte()
    
    def fabricarSur(self):
        return Sur()
    
    def fabricarEste(self):
        return Este()
    
    def fabricarOeste(self):
        return Oeste()
    
    def fabricarBichoAgresivo(self):
        bicho=Bicho()
        bicho.modo=Agresivo()
        bicho.iniAgresivo()
        return bicho
    
    def fabricarBichoPerezoso(self):
        bicho=Bicho()
        bicho.modo=Perezoso()
        bicho.iniPerezoso()
        return bicho
    
    def fabricarBichoSabio(self):
        bicho=Bicho()
        bicho.modo=Sabio()
        bicho.iniSabio()
        return bicho

    def obtenerJuego(self):
        return self.juego
    
    def fabricarBicho(self,modo,posicion):
        
        if modo=='Agresivo':
            bicho=self.fabricarBichoAgresivo()
        if modo=='Perezoso':
            bicho=self.fabricarBichoPerezoso()
        if modo=='Sabio':
            bicho=self.fabricarBichoSabio()

        hab=self.laberinto.obtenerHabitacion(posicion)
        hab.entrar(bicho)
        self.juego.agregar_bicho(bicho)