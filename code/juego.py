from abc import ABC, abstractmethod

class ElementoMapa:
    def __init__(self):
        pass

    def entrar(self):
        pass



class Creator:
    def crear_habitacion(self, num):
        habitacion = Habitacion(num)
        habitacion.norte = self.fabricar_pared()
        habitacion.sur = self.fabricar_pared()
        habitacion.este = self.fabricar_pared()
        habitacion.oeste = self.fabricar_pared()
        return habitacion

    def fabricar_laberinto(self):
        return Laberinto()

    def fabricar_pared(self):
        return Pared()

    def fabricar_puerta(self, lado1, lado2):
        return Puerta(lado1, lado2)

class CreatorB(Creator):

    def fabricar_pared(self):
        return ParedBomba()

class CreatorBlind(Creator):

    def fabricar_puerta(self, lado1, lado2):
        return PuertaBlindada(lado1, lado2)


class Decorator(ElementoMapa):
    def __init__(self, em):
        super().__init__()
        self.em = em

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

## ------------------------------------------------------
class Blindaje(Decorator):

    def __init__(self, em):
        super().__init__(em)
        self.blindaje = False

    def blindar(self):
        print("Aplicando blindaje")
        self.blindaje = True

    def estaBlindada(self):
        return self.blindaje


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



class Habitacion(ElementoMapa):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def entrar(self):
        print(f"Entrando en la habitación {self.num}")

class Laberinto(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.habitaciones = []

    def entrar(self):
        print("Entrando en el laberinto")

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def obtenerHabitacion(self, num):
        for habitacion in self.habitaciones:
            if habitacion.num == num:
                return habitacion
        return None

class Pared(ElementoMapa):
    def __init__(self):
        super().__init__()

    def entrar(self):
        print("Entrando en una pared")

class ParedBomba(Pared):
    def __init__(self):
        super().__init__()
        self.activa = False

    def entrar(self):
        print("Entrando en una pared bomba")


class Puerta:
    def __init__(self, lado1, lado2):
        self.abierta = False
        self.lado1 = lado1
        self.lado2 = lado2

    def entrar(self):
        print("Entrando en una puerta")

    def abrir(self):
        self.abierta = True

    def cerrar(self):
        self.abierta = False

class PuertaBlindada(Puerta):

    def __init__(self,lado1, lado2):
        super().__init__(lado1, lado2)
        self.blidada = True

    def entrar(self):
        print("Entrando en una puerta blindada")


class Juego:
    def __init__(self):
        self.laberinto = Laberinto()
        self.bichos = []

    def agregar_bicho(self, bicho):
        self.bichos.append(bicho)

    def iniciar_juego(self):
        # Lógica para iniciar el juego
        pass

    def crear_laberinto2_hab_fm(self, creator):
        laberinto = creator.crear_laberinto()
        habitacion1 = creator.crear_habitacion(1)
        habitacion2 = creator.crear_habitacion(2)
        puerta = creator.crear_puerta(habitacion1, habitacion2)
        habitacion1.sur = puerta
        habitacion2.norte = puerta
        laberinto.agregar_habitacion(habitacion1)
        laberinto.agregar_habitacion(habitacion2)
        return laberinto

    def crear_laberinto_2hab_bomba(self, creator):
        laberinto = creator.crear_laberinto()
        habitacion1 = creator.crear_habitacion(1)
        habitacion2 = creator.crear_habitacion(2)
        puerta = creator.crear_puerta(habitacion1, habitacion2)

        habitacion1.sur = puerta
        habitacion2.norte = puerta

        pared1 = creator.crear_pared()
        bomba1 = creator.crear_bomba(pared1)
        habitacion1.este = bomba1

        pared2 = creator.crear_pared()
        bomba2 = creator.crear_bomba(pared2)
        habitacion2.oeste = bomba2

        laberinto.agregar_habitacion(habitacion1)
        laberinto.agregar_habitacion(habitacion2)
        return laberinto

    def obtener_habitacion(self, num):
        return self.laberinto.obtenerHabitacion(num)

    def crear_laberinto_4hab(self, creator):
        laberinto = creator.crear_laberinto()

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