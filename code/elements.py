from abc import ABC, abstractmethod

class ElementoMapa:
    def __init__(self):
        pass

    def entrar(self):
        pass

# TODO: MAP'S ELEMENTS

class Habitacion(ElementoMapa):

    def __init__(self, num):
        super().__init__()
        self.num = num
        self.norte = None
        self.sur = None
        self.oeste = None
        self.este = None


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
    
class Decorator(ElementoMapa):
    def __init__(self, em):
        super().__init__()
        self.em = em




class Blindaje(Decorator):

    def __init__(self, em):
        super().__init__(em)
        self.blindaje = False

    def blindar(self):
        print("Aplicando blindaje")
        self.blindaje = True

    def estaBlindada(self):
        return self.blindaje



