from contenedor import Contenedor

class Habitacion(Contenedor):

    def __init__(self, num):
        super().__init__()
        self.num = num
        self.longitud = 0

    def recorrer(self, unBloque: list):
        super().recorrer_preorden(unBloque)


    def entrar(self):
        print(f"Entrando en la habitación {self.num}")

    def __str__(self):
        return "Soy una habitación"