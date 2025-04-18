from abc import ABC
from code.elemento_mapa import *
from creator import *


class Juego:
    def __init__(self):
        self.laberinto = Laberinto()
        self.bichos = []

    def agregar_bicho(self, bicho):
        self.bichos.append(bicho)

    def iniciar_juego(self):
        # Lógica para iniciar el juego
        pass

    def crear_laberinto2_hab_fm(self, creator:Creator):
        laberinto = creator.fabricar_laberinto()
        habitacion1 = creator.crear_habitacion(1)
        habitacion2 = creator.crear_habitacion(2)
        puerta = creator.fabricar_puerta(habitacion1, habitacion2)
        habitacion1.sur = puerta
        habitacion2.norte = puerta
        laberinto.agregar_habitacion(habitacion1)
        laberinto.agregar_habitacion(habitacion2)
        return laberinto

    def crear_laberinto_2hab_bomba(self, creator:Creator):
        laberinto = creator.fabricar_laberinto()
        habitacion1 = creator.crear_habitacion(1)
        habitacion2 = creator.crear_habitacion(2)
        puerta = creator.fabricar_puerta(habitacion1, habitacion2)

        habitacion1.sur = puerta
        habitacion2.norte = puerta

        pared1 = creator.fabricar_pared()
        bomba1 = creator.crear_bomba(pared1)
        habitacion1.este = bomba1

        pared2 = creator.fabricar_pared()
        bomba2 = creator.crear_bomba(pared2)
        habitacion2.oeste = bomba2

        laberinto.agregar_habitacion(habitacion1)
        laberinto.agregar_habitacion(habitacion2)
        return laberinto

    def obtener_habitacion(self, num):
        return self.laberinto.obtenerHabitacion(num)

    def crear_laberinto_4hab(self, creator:Creator):
        laberinto = creator.fabricar_laberinto

        habitacion1 = creator.crear_habitacion(1)
        habitacion2 = creator.crear_habitacion(2)
        habitacion3 = creator.crear_habitacion(3)
        habitacion4 = creator.crear_habitacion(4)

        puerta12 = creator.crear_puerta(habitacion1, habitacion2)
        puerta13 = creator.crear_puerta(habitacion1, habitacion3)
        puerta24 = creator.crear_puerta(habitacion2, habitacion4)
        puerta34 = creator.crear_puerta(habitacion3, habitacion4)

        habitacion1.sur = puerta12
        habitacion1.este = puerta13
        habitacion3.oeste = puerta13
        habitacion3.sur = puerta34
        habitacion2.norte = puerta12
        habitacion2.este = puerta24
        habitacion4.norte = puerta34
        habitacion4.oeste = puerta24

        bicho1 = creator.crear_bicho(5, 10, habitacion1, creator.crear_modo_agresivo())
        self.agregar_bicho(bicho1)
        bicho3 = creator.crear_bicho(5, 10, habitacion3, creator.crear_modo_agresivo())
        self.agregar_bicho(bicho3)
        bicho2 = creator.crear_bicho(5, 1, habitacion2, creator.crear_modo_perezoso())
        self.agregar_bicho(bicho2)
        bicho4 = creator.crear_bicho(5, 1, habitacion4, creator.crear_modo_perezoso())
        self.agregar_bicho(bicho4)

        habitacion1.bicho = bicho1
        habitacion2.bicho = bicho2
        habitacion3.bicho = bicho3
        habitacion4.bicho = bicho4

        laberinto.agregar_habitacion(habitacion1)
        laberinto.agregar_habitacion(habitacion2)
        laberinto.agregar_habitacion(habitacion3)
        laberinto.agregar_habitacion(habitacion4)

        return laberinto