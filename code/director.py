from abc import ABC, abstractmethod
import json
from laberinto_builder import LaberintoBuilder
from habitacion import Habitacion
from puerta import Puerta

class Director(ABC):

    def __init__(self, fichero):
        self.procesar(fichero)
        self.builderLab = LaberintoBuilder()
        

    
    def procesar(self, fichero):
        laberinto = None
        puertas = None
        bichos = None
        with open(fichero, 'r') as archivo:
            datos = json.load(archivo)
        
    
    def procesar_laberinto(self, laberinto):

        self.laberinto = laberinto
        "TODO: Controlar otros tipos como  pared"
        for i in laberinto:
            if i.get('tipo') == 'habitacion':
                habitacion = Habitacion(i.get('num'))
                self.builderLab.agregar_habitacion(habitacion)

    def __init__(self):
        self.builderLab = None
        self.dict=None

    def obtenerJuego(self):
        return self.builderLab.obtenerJuego()
    
    def procesar(self,fichero):
        self.procesarFichero(fichero)
        self.iniciarBuilder()
        self.fabricarLaberinto()
        self.fabricarJuego()
        self.fabricarBichos()

    def fabricarJuego(self):
        self.builderLab.fabricarJuego()
        return self

    def iniciarBuilder(self):
        if self.dict['forma']=='cuadrado':
             self.builder=LaberintoBuilder()
        return self

    def fabricarLaberinto(self):
        self.builderLab.fabricarLaberinto()
        for i in self.dict['laberinto']:
            self.fabricarLaberintoRecursivo(i,'root')
        
        for i in self.dict['puertas']:
            self.builderLab.fabricarPuerta(i[0],i[1],i[2],i[3]) 
        
        return self
	
    def fabricarLaberintoRecursivo(self,l,padre):
        print(l)
        if l['tipo']=='habitacion':
            con=self.builderLab.fabricarHabitacion(l['num'])
        
        if l['hijos']!=None:
            for cadaUno in l['hijos']:
                self.fabricarLaberintoRecursivo(cadaUno,con)

        return self

    def procesarFichero(self, ruta):
        try:
            with open(ruta, 'r') as f:
                data = json.load(f)
            self.dict=data
            return data
        except FileNotFoundError:
            print(f"Error: Fichero no encontrado: {ruta}")
            return None

    def fabricarBichos(self):
        for b in self.dict['bichos']:
            self.builderLab.fabricarBicho(b['modo'],b['posicion'])

        return self

        