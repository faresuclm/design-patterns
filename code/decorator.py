from elements import ElementoMapa

class Hoja(ElementoMapa):

    def __init__(self):
        super().__init__()

class Decorator(Hoja):
    
    def __init__(self, em):
        super().__init__()
        self.em = em


class Hoja(ElementoMapa):

    def __init__(self, em):
        super().__init__(em)




class Blindaje(Decorator):

    def __init__(self, em):
        super().__init__(em)
        self.blindado = False

    def blindar(self):
        print("Aplicando blindaje")
        self.blindado = True

    def estaBlindada(self):
        return self.blindado