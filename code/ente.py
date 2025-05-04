class Ente:
    def __init__(self):
        self.vidas = None
        self.poder = None
        self.posicion = None
        self.juego = None


class EstadoEnte:

    def __init__(self):
        super().__init__()

class Vivo(EstadoEnte):
    def __init__(self):
        super().__init__()

class Muerto(EstadoEnte):
    def __init__(self):
        super().__init__()

class Personaje(Ente):
    def __init__(self, vidas, poder, juego, nombre):        
        self.nombre = nombre