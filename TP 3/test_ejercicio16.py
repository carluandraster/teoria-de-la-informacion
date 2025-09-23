import unittest
from ejercicio16 import simular_fuente

# BEGIN: Test Cases
class TestSimularFuente(unittest.TestCase):
    def test_simular_fuente_basic(self):
        codigos = ['A', 'B', 'C']
        probabilidades = [0.2, 0.5, 0.3]
        n = 10
        resultado = simular_fuente(codigos, probabilidades, n)
        self.assertEqual(len(resultado), n)
        for simbolo in resultado:
            self.assertIn(simbolo, codigos)

    def test_simular_fuente_single_symbol(self):
        codigos = ['A']
        probabilidades = [1.0]
        n = 5
        resultado = simular_fuente(codigos, probabilidades, n)
        self.assertEqual(resultado, ['A'] * n)

# END: Test Cases