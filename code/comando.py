

class Comando:
    
    def __init__(self, receptor):
        self.receptor = receptor

    def ejecutar(self):
        pass
    
class ComandoAbrir(Comando):
    def ejecutar(self):
        self.receptor.abrir()
        print("Abrir ejecutado.")

    
class ComandoCerrar(Comando):
    def ejecutar(self):
        self.receptor.cerrar()
        print("Cerrar ejecutado.")

class ComandoEntrar(Comando):
    def ejecutar(self):
        self.receptor.entrar()
        print("Entrar ejecutado.")

class ComandoActivar(Comando):
    def ejecutar(self):
        self.receptor.activar()
        print("Activar ejecutado.")