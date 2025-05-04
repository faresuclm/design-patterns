from elemento_mapa import ElementoMapa

class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2):
        self.abierta = False
        self.lado1 = lado1
        self.lado2 = lado2
        self.longitud = 0
        self.estado = EstadoPuerta()

    def entrar(self):
        print("Entrando en una puerta")

    def abrir(self):
        self.abierta = True

    def cerrar(self):
        self.abierta = False


class EstadoPuerta:

    def __init__(self):
        super().__init__()

class Abierta(EstadoPuerta):

    def __init__(self):
        super().__init__()

    def entrar(self):
        print("Estado de la puerta: Abierta")

class Cerrada(EstadoPuerta):
    def __init__(self):
        super().__init__()

    def entrar(self):
        print("Estado de la puerta: Cerrada")


class PuertaBlindada(Puerta):

    def __init__(self,lado1, lado2):
        super().__init__(lado1, lado2)
        self.blidada = True

    def entrar(self):
        print("Entrando en una puerta blindada")