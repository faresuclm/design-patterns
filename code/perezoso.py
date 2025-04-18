from modo import Modo

class Perezoso(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self, bicho):
        print("Perezoso: Dormir es lo más importante para mí...")

    def caminar(self, bicho):
        print("Perezoso: Ufff que pereeza caminar, mejor me quedo aquí...")

    def atacar(self, bicho):
        print("Perezoso: Atacar? No, gracias. Prefiero dormir...")

    def sanar(self, bicho):
        print("Perezoso: Bueno, sanar es fácil, sólo me quedo quieto y espero a que pase el tiempo...")

    def autodestruir(self, bicho):
        print("Perezoso: Ha llegado el momento de autodestruirme, por fin podré descansar...")