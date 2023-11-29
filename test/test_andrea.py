import unittest
from utilities import utilities

class TestUtilities(unittest.TestCase):
    
     def test_afeccion_sana(self):
         """ Prueba cuando una afeccion es sana"""
         Valor = 330
         result = utilities.nivelAfeccion(Valor)
         self.assertAlmostEqual("sano", result)