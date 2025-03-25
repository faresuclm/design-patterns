from elements import ElementoMapa

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