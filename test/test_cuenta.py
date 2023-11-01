import unittest
from cuenta import Cuenta

class TestCuenta(unittest.TestCase):
    
    def test_retiro_menos_saldo(self):
        """ Prueba un retiro normal, con un valor mnenor al saldo"""
        cuenta = Cuenta(500000)
        resultado_retiro = cuenta.retirar(200000)
        
        self.assertTrue(resultado_retiro)
        self.assertEqual(300000,cuenta.saldo)
    
    def test_retiro_mayor_saldo(self):
        """ Prueba un retiro normal, con un valor mayor al saldo"""
        cuenta = Cuenta(500000)
        resultado_retiro = cuenta.retirar(700000)
        
        self.assertFalse(resultado_retiro)
        self.assertEqual(500000,cuenta.saldo)
    
    def test_cantidad_negativa(self):
        """ Prueba un retiro normal, con un valor mayor al saldo"""
        cuenta = Cuenta(500000)
        with self.assertRaises(ValueError):
            cuenta.retirar(-100000)
        
        self.assertEqual(500000,cuenta.saldo)