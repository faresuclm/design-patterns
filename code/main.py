
from juego import *
from creator import *

#ejemplo de uso
fm = Creator()
juego = Juego()
juego.laberinto = juego.crear_laberinto2_hab_fm(fm)
hab1=juego.obtener_habitacion(1)
hab2=juego.obtener_habitacion(2)
print(hab1.num)
print(hab2.num)