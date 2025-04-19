from contenedor import Contenedor
from habitacion import Habitacion

class Laberinto(Contenedor):
    def __init__(self):
        super().__init__()
        self.habitaciones = []

    def entrar(self):
        print("Entrando en el laberinto")

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def obtenerHabitacion(self, num) -> Habitacion:
        for habitacion in self.habitaciones:
            if habitacion.num == num:
                return habitacion
        return None