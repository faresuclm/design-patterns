from modo import Modo

class Agresivo(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self, bicho):
        print("Agresivo: Durmiendo un poco, pero no puedo bajar la guardia...")

    def caminar(self, bicho):
        print("Agresivo: Caminando con determinación, acabaré con todos aquí...")

    def atacar(self, bicho):
        print("Agresivo: 'Sentid la ira espartana!")

    def sanar(self, bicho):
        print("Agresivo: No necesito sanar, soy un guerrero imbatible!")

    def autodestruir(self, bicho):
        print("Agresivo: 'No me rendiré, autodestruirse no es una opción!")