from abc import ABC, abstractmethod

class ElementoMapa:
    
    def __init__(self):
        pass

    def entrar(self):
        pass

    def recorrer(self, unBloque: list):
        pass

    def recorrer_preorden(self, unBloque: list, indice = 0):
        nodo_actual = None
        if unBloque is None:
            print("Bloque vacio")
        else:
            nodo_actual = unBloque[indice]
            nodo_actual.entrar()
            self.recorrer_preorden(unBloque, 2*indice + 1)
            self.recorrer_preorden(unBloque, 2*indice + 2)
    
    def recorrer_inorden(self, unBloque: list, indice = 0):
        nodo_actual = None
        if unBloque is None:
            print("Bloque vacio")
        else:
            nodo_actual = unBloque[indice]
            self.recorrer_inorden(unBloque, 2*indice + 1)
            nodo_actual.entrar()
            self.recorrer_inorden(unBloque, 2*indice + 2)


    def recorrer_postorden(self, unBloque: list, indice = 0):
        nodo_actual = None
        if unBloque is None:
            return "Bloque vacio"
        else:
            nodo_actual = unBloque[indice]
            self.recorrer_postorden(unBloque, 2*indice + 1)
            self.recorrer_postorden(unBloque, 2*indice + 2)
            nodo_actual.entrar()

    def recorrer_bf(self, unBloque: list):
        if unBloque is None:
            print("Bloque vacio")
        else:
            for i in range(len(unBloque)):
                nodo_actual = unBloque[i]
                nodo_actual.entrar()

        



