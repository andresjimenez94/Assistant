import unittest
import utilities

class TestUtilities(unittest.TestCase):
    
    def test_afeccion_sana(self):
        """ Prueba cuando una afeccion es sana"""
        Valor = 330
        result = utilities.nivelAfeccion(Valor)
        self.assertAlmostEqual("sano", result)

    def test_afeccion_enfermo(self):
        """ Prueba cuando una afeccion es enfermo"""
        Valor = 521
        result = utilities.nivelAfeccion(Valor)
        self.assertAlmostEqual("enfermo", result)
    
    def test_afeccion_grave(self):
        """ Prueba cuando una afeccion es grave"""
        Valor = 1100
        result = utilities.nivelAfeccion(Valor)
        self.assertAlmostEqual("grave", result)
    
    def test_afeccion_fuera_rango(self):
        """ Prueba cuando una afeccion es grave"""
        Valor = 0
        result = utilities.nivelAfeccion(Valor)
        self.assertAlmostEqual("fuera de rango", result)