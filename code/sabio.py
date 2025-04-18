from modo import Modo

class Sabio(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self, bicho):
        print("Sabio: Mi cuerpo necesita reposo pero no puedo bajar la guardia...")

    def caminar(self, bicho):
        print("Sabio: Caminando con cautela...")

    def atacar(self, bicho):
        print("Sabio: Debo utilizar cada ataque con sabiduría y dosificar...")

    def sanar(self, bicho):
        print("Sabio: La sabiduría es la mejor medicina...")

    def autodestruir(self, bicho):
        print("Sabio: La autodestrucción es un último recurso...")