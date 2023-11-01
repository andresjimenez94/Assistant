import unittest
import restaurante

class TestRestaurante(unittest.TestCase):
    
     def test_buscar_plato_existe(self):
         #MenuPlatos = [("frijoles",5000.0), ("sopa",6000.0), ("lentejas",4000.0)]
         resultado_buscar_plato = restaurante.BuscarPlato("frijoes")
         self.assertTrue(resultado_buscar_plato)