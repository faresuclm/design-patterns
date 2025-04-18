from elements import ElementoMapa

class Contenedor(ElementoMapa):

    def __init__(self):
        super().__init__()
        self.hijos = list()
        self.orientaciones = list()
        self.longitud = 0
    

    def entrar(self):
        return super().entrar()
    

    def agregar_hijo(self, hijo):
        hijo.padre= self
        self.hijos.append(hijo)

    
    def eliminar_hijo(self, hijo):
        self.hijos.remove(hijo)

    def cabe_dentro_de(self, otro):
        pass
        
        
        

    
    def agregarOrientacion(self, orientacion):
        self.orientaciones.append(orientacion)

    
    def eliminarOrientacion(self, orientacion):
        self.orientaciones.remove(orientacion)

    
    def __str__(self):
        return "Soy un contenedor"