import unittest
from laberinto_builder import LaberintoBuilder

class TestLaberintoBuilder(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.builder = LaberintoBuilder()

    def test_obtenerHabitacion(self, numero = 1):
        hab = self.builder.laberinto.obtenerHabitacion(numero)
        self.assertEqual(hab.num, numero)

    def test_init(self):
        self.assertIsNone(self.builder.laberinto)
        self.assertIsNone(self.builder.juego)

    def test_fabricarJuego(self):
        self.builder.fabricarJuego()
        self.assertIsNotNone(self.builder.juego)
        self.assertEqual(type(self.builder.juego).__name__, 'Juego')

    def test_fabricarLaberinto(self):
        self.builder.fabricarLaberinto()
        self.assertIsNotNone(self.builder.laberinto)
        self.assertEqual(type(self.builder.laberinto).__name__, 'Laberinto')

    @classmethod
    def tearDownClass(self):
        del self.builder