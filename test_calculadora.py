import unittest
from calculadora import calcular

class TestCalcularcalcular(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(calcular(5, 3, '+'), 8)
        self.assertEqual(calcular(-5, 3, '+'), -2)
        self.assertEqual(calcular(5.5, 2.5, '+'), 8.0)

    def test_subtracao(self):
        self.assertEqual(calcular(5, 3, '-'), 2)
        self.assertEqual(calcular(-5, 3, '-'), -8)
        self.assertEqual(calcular(5.5, 2.5, '-'), 3.0)

    def test_multiplicacao(self):
        self.assertEqual(calcular(5, 3, '*'), 15)
        self.assertEqual(calcular(-5, 3, '*'), -15)
        self.assertEqual(calcular(5.5, 2, '*'), 11.0)

    def test_divisao(self):
        self.assertEqual(calcular(6, 3, '/'), 2)
        self.assertEqual(calcular(-6, 3, '/'), -2)
        self.assertEqual(calcular(5, 2, '/'), 2.5)

    def test_divisao_por_zero(self):
        self.assertIsNone(calcular(5, 0, '/'))

    def test_potenciacao(self):
        self.assertEqual(calcular(2, 3, '^'), 8)
        self.assertEqual(calcular(5, 0, '^'), 1)
        self.assertEqual(calcular(4, 0.5, '^'), 2)

    def test_operacao_invalida(self):
        self.assertIsNone(calcular(5, 3, '%'))

    def test_valores_nao_numericos(self):
        self.assertIsNone(calcular('a', 3, '+'))
        self.assertIsNone(calcular(5, 'b', '+'))
        self.assertIsNone(calcular('a', 'b', '+'))

if __name__ == '__main__':
    unittest.main()
