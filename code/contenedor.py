from elemento_mapa import ElementoMapa

class Contenedor(ElementoMapa):

    def __init__(self):
        super().__init__()
        self.hijos = list()
        self.orientaciones = list()
        self.longitud = 0
        self.forma:Forma = None
    

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
        self.forma.agregarOrientacion(orientacion)

    
    def eliminarOrientacion(self, orientacion):
        self.forma.eliminarOrientacion(orientacion)

    def ponerElementoEnOrientacion(self, elemento, orientacion):
        self.forma.ponerElementoEnOrientacion(elemento, orientacion)

    def obtenerElementoEnOrientacion(self, orientacion):
         return self.forma.obtenerElementoEnOrientacion(orientacion)

    
    def __str__(self):
        return "Soy un contenedor"
    

class Forma:

    def __init__(self):
        super().__init__()
        self.orientaciones = list()

    def agregarOrientacion(self, orientacion):
        self.orientaciones.append(orientacion)
 
    def eliminarOrientacion(self, orientacion):
        self.orientaciones.remove(orientacion)
 
    def ponerElementoEnOrientacion(self, elemento, orientacion):
        orientacion.poner(elemento, self)
 
    def obtenerElementoEnOrientacion(self, orientacion):
        return orientacion.obtenerElemento(self)



class Cuadrado(Forma):

    def __init__(self):
        super().__init__()
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None


class Rombo(Forma):

    def __init__(self):
        super().__init__()
        self.noreste = None
        self.noroeste = None
        self.sureste = None
        self.suroeste = None