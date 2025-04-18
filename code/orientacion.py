
from contenedor import Contenedor

class Orientacion(Contenedor):

    def __init__(self):
        super().__init__()
        self.norte = None
        self.sur = None
        self.oeste = None
        self.este = None


class Norte(Orientacion):

    def __init__(self):
        super().__init__()

    
    def __str__(self):
        return "Soy la orientación norte"
    

class Sur(Orientacion):

    def __init__(self):
        super().__init__()

    
    def __str__(self):
        return "Soy la orientación sur"
    

class Oeste(Orientacion):

    def __init__(self):
        super().__init__()


    def __str__(self):
        return "Soy la orientación oeste"
    

class Este(Orientacion):

    def __init__(self):
        super().__init__()

    
    def __str__(self):
        return "Soy la orientación este"