from elements import ElementoMapa

class Puerta(ElementoMapa):
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