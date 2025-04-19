
from contenedor import Contenedor

class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

class Orientacion(Contenedor):
    
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def poner(self, contenedor, elemento):
        pass

    def __init__(self):
        super().__init__()
        self.norte = None
        self.sur = None
        self.oeste = None
        self.este = None


class Norte(Orientacion):

    def __init__(self):
        super().__init__()

    
    def poner(self, contenedor, elemento):
        contenedor.norte = elemento

    
    def __str__(self):
        return "Soy la orientación norte"
    

class Sur(Orientacion):

    def __init__(self):
        super().__init__()

    def poner(self, contenedor, elemento):
        contenedor.sur = elemento
    
    def __str__(self):
        return "Soy la orientación sur"
    

class Oeste(Orientacion):

    def __init__(self):
        super().__init__()

    
    def poner(self, contenedor, elemento):
        contenedor.oeste = elemento


    def __str__(self):
        return "Soy la orientación oeste"
    

class Este(Orientacion):

    def __init__(self):
        super().__init__()

    def poner(self, contenedor, elemento):
        contenedor.este = elemento

    
    def __str__(self):
        return "Soy la orientación este"