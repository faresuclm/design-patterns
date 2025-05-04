import abc

# --- Patrón State ---
class EstadoEnte(abc.ABC):
    @abc.abstractmethod
    def actuar(self, ente):
        pass

class Vivo(EstadoEnte):
    def actuar(self, ente):
        print(f"{ente.nombre} está vivo y actuando.")

class Muerto(EstadoEnte):
    def actuar(self, ente):
        print(f"{ente.nombre} está muerto y no puede actuar.")

class EstadoPuerta(abc.ABC):
    @abc.abstractmethod
    def interactuar(self, puerta):
        pass

class Abierta(EstadoPuerta):
    def interactuar(self, puerta):
        print(f"La puerta {puerta.id} está abierta.")
        puerta.estado = Cerrada()

class Cerrada(EstadoPuerta):
    def interactuar(self, puerta):
        print(f"La puerta {puerta.id} está cerrada.")
        puerta.estado = Abierta()

# --- Clases base ---
class Ente:
    def __init__(self, nombre, vidas=1, poder=1):
        self.nombre = nombre
        self.vidas = vidas
        self.poder = poder
        self.estado = Vivo()

    def actuar(self):
        self.estado.actuar(self)

class Personaje(Ente):
    def __init__(self, nombre, vidas=1, poder=1):
        super().__init__(nombre, vidas, poder)

class Bicho(Ente):
    def __init__(self, nombre, vidas=1, poder=1):
        super().__init__(nombre, vidas, poder)
        self.modo = None # Podría implementar un patrón Strategy aquí

    def atacar(self):
        print(f"{self.nombre} está atacando.")

    def domir(self):
        print(f"{self.nombre} se ha dormido.")

    def cambiar_modo(self, modo):
        self.modo = modo
        print(f"{self.nombre} cambia a modo {modo}.")

class ElementoMapa(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def mostrar(self):
        pass

class Contenedor(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.hijos = []

    def agregar(self, elemento):
        self.hijos.append(elemento)

    def eliminar(self, elemento):
        self.hijos.remove(elemento)

    def mostrar(self):
        for hijo in self.hijos:
            hijo.mostrar()

class Hoja(ElementoMapa):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def mostrar(self):
        print(f"  - {self.nombre}")

class Pared(Hoja):
    def __init__(self, lado1, lado2):
        super().__init__(f"Pared ({lado1}, {lado2})")

class Puerta(Hoja):
    def __init__(self, id):
        super().__init__(f"Puerta {id}")
        self.id = id
        self.estado = Cerrada()

    def interactuar(self):
        self.estado.interactuar(self)

class Bomba(Hoja):
    def __init__(self):
        super().__init__("Bomba")

    def activa(self):
        print("¡Bomba activada!")

class Tunel(Hoja):
    def __init__(self, laberinto):
        super().__init__("Túnel")
        self.laberinto_destino = laberinto

    def entrar(self):
        print(f"Entrando al túnel hacia el laberinto {self.laberinto_destino.nombre}.")

class ParedBomba(Hoja):
    def __init__(self):
        super().__init__("Pared con Bomba")
        self.bomba = Bomba()

    def activa(self):
        self.bomba.activa()

class Habitacion(Contenedor):
    def __init__(self, numero):
        super().__init__()
        self.numero = numero

    def mostrar(self):
        print(f"Habitación {self.numero}:")
        super().mostrar()

class Armario(Contenedor):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def mostrar(self):
        print(f"Armario {self.num}:")
        super().mostrar()

class Laberinto(Contenedor):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def mostrar(self):
        print(f"Laberinto: {self.nombre}")
        super().mostrar()

# --- Patrón Command ---
class Comando(abc.ABC):
    def __init__(self, receptor):
        self.receptor = receptor

    @abc.abstractmethod
    def ejecutar(self):
        pass

class Entrar(Comando):
    def ejecutar(self):
        self.receptor.entrar()

class Activar(Comando):
    def ejecutar(self):
        self.receptor.activa()

class Abrir(Comando):
    def ejecutar(self):
        self.receptor.interactuar() # Asumiendo que el receptor tiene un método interactuar

class Cerrar(Comando):
    def ejecutar(self):
        self.receptor.interactuar() # Asumiendo que el receptor tiene un método interactuar

# --- Patrón Decorator ---
class DecoradorComando(Comando):
    def __init__(self, comando):
        self.comando = comando
        super().__init__(comando.receptor)

    def ejecutar(self):
        self.comando.ejecutar()

class ComandoActivar(DecoradorComando):
    def ejecutar(self):
        print("Preparando para activar...")
        super().ejecutar()
        print("Comando de activación completado.")

# --- Patrón Builder ---
class LaberintoBuilder(abc.ABC):
    def __init__(self):
        self.laberinto = None

    def obtener_laberinto(self):
        return self.laberinto

    def crear_laberinto(self, nombre):
        self.laberinto = Laberinto(nombre)

    @abc.abstractmethod
    def construir_habitacion(self, numero):
        pass

    @abc.abstractmethod
    def construir_pared(self, habitacion1, lado1, habitacion2, lado2):
        pass

    @abc.abstractmethod
    def construir_puerta(self, habitacion1, habitacion2):
        pass

class LaberintoBuilderRombo(LaberintoBuilder):
    def construir_habitacion(self, numero):
        habitacion = Habitacion(numero)
        self.laberinto.agregar(habitacion)
        return habitacion

    def construir_pared(self, habitacion1, lado1, habitacion2, lado2):
        pared = Pared(lado1, lado2)
        habitacion1.agregar(pared)
        habitacion2.agregar(pared)

    def construir_puerta(self, habitacion1, habitacion2):
        puerta = Puerta(len(self.laberinto.hijos)) # ID basado en el número de puertas
        habitacion1.agregar(puerta)
        habitacion2.agregar(puerta)

class Director:
    def __init__(self):
        self.builder = None

    def construir_laberinto(self, builder, nombre):
        self.builder = builder
        self.builder.crear_laberinto(nombre)
        self.builder.construir_habitacion(1)
        self.builder.construir_habitacion(2)
        self.builder.construir_pared(self.builder.laberinto.hijos[0], "Norte", self.builder.laberinto.hijos[1], "Sur")
        self.builder.construir_puerta(self.builder.laberinto.hijos[0], self.builder.laberinto.hijos[1])
        return self.builder.obtener_laberinto()

# --- Patrón Factory Method (Simplificado) ---
class Creator(abc.ABC):
    @abc.abstractmethod
    def fabricar_laberinto(self, nombre):
        pass

    @abc.abstractmethod
    def fabricar_pared(self, lado1, lado2):
        pass

    @abc.abstractmethod
    def fabricar_puerta(self, id):
        pass

    @abc.abstractmethod
    def fabricar_habitacion(self, numero):
        pass

class CreatorB(Creator):
    def fabricar_laberinto(self, nombre):
        return Laberinto(nombre)

    def fabricar_pared(self, lado1, lado2):
        return Pared(lado1, lado2)

    def fabricar_puerta(self, id):
        return Puerta(id)

    def fabricar_habitacion(self, numero):
        return Habitacion(numero)

# --- Juego y Fase (Simplificado) ---
class Fase:
    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []

    def agregar_elemento(self, elemento):
        self.elementos.append(elemento)

    def mostrar(self):
        print(f"--- Fase: {self.nombre} ---")
        for elemento in self.elementos:
            elemento.mostrar()

class Juego:
    def __init__(self, nombre):
        self.nombre = nombre
        self.fases = []
        self.jugador = None

    def agregar_fase(self, fase):
        self.fases.append(fase)

    def asignar_jugador(self, jugador):
        self.jugador = jugador
        print(f"El jugador {self.jugador.nombre} ha entrado al juego.")

    def iniciar(self):
        print(f"¡Iniciando el juego: {self.nombre}!")
        if self.jugador:
            print(f"Bienvenido, {self.jugador.nombre}.")
        for fase in self.fases:
            fase.mostrar()

# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Crear un laberinto usando el Builder
    director = Director()
    laberinto_builder = LaberintoBuilderRombo()
    laberinto_rombo = director.construir_laberinto(laberinto_builder, "Laberinto Romboide")
    laberinto_rombo.mostrar()
    print("\n")

    # Crear elementos usando el Factory Method
    creator_b = CreatorB()
    pared_nueva = creator_b.fabricar_pared("Este", "Oeste")
    puerta_secreta = creator_b.fabricar_puerta("S3CR3T0")
    habitacion_final = creator_b.fabricar_habitacion(99)
    print(f"Pared creada: {pared_nueva.nombre}")
    puerta_secreta.interactuar()
    print(f"Habitación creada: {habitacion_final.numero}")
    print("\n")

    # Usar el patrón Command y Decorator
    tunel_escape = Tunel(laberinto_rombo)
    comando_entrar = Entrar(tunel_escape)
    comando_activar_bomba = Activar(Bomba())
    comando_activar_decorado = ComandoActivar(comando_activar_bomba)

    print("Ejecutando comandos:")
    comando_entrar.ejecutar()
    comando_activar_decorado.ejecutar()
    print("\n")

    # Crear personajes y usar el patrón State
    personaje_principal = Personaje("Héroe", vidas=3)
    enemigo = Bicho("Goblin")
    enemigo.cambiar_modo("Agresivo")

    personaje_principal.actuar()
    enemigo.actuar()
    enemigo.atacar()
    personaje_principal.vidas -= 1
    if personaje_principal.vidas == 0:
        personaje_principal.estado = Muerto()
    personaje_principal.actuar()
    print("\n")

    # Crear un juego y fases
    fase_inicial = Fase("Entrada")
    fase_inicial.agregar_elemento(laberinto_rombo)
    fase_inicial.agregar_elemento(personaje_principal)

    juego_principal = Juego("Aventura en Albacete")
    juego_principal.agregar_fase(fase_inicial)
    juego_principal.asignar_jugador(personaje_principal)
    juego_principal.iniciar()