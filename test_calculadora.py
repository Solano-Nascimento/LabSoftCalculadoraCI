import unittest
from calculadora import calculadora

class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(calculadora(5, 3, '+'), 8)
        self.assertEqual(calculadora(-5, 3, '+'), -2)
        self.assertEqual(calculadora(5.5, 2.5, '+'), 8.0)

    def test_subtracao(self):
        self.assertEqual(calculadora(5, 3, '-'), 2)
        self.assertEqual(calculadora(-5, 3, '-'), -8)
        self.assertEqual(calculadora(5.5, 2.5, '-'), 3.0)

    def test_multiplicacao(self):
        self.assertEqual(calculadora(5, 3, '*'), 15)
        self.assertEqual(calculadora(-5, 3, '*'), -15)
        self.assertEqual(calculadora(5.5, 2, '*'), 11.0)

    def test_divisao(self):
        self.assertEqual(calculadora(6, 3, '/'), 2)
        self.assertEqual(calculadora(-6, 3, '/'), -2)
        self.assertEqual(calculadora(5, 2, '/'), 2.5)

    def test_divisao_por_zero(self):
        self.assertIsNone(calculadora(5, 0, '/'))

    def test_potenciacao(self):
        self.assertEqual(calculadora(2, 3, '^'), 8)
        self.assertEqual(calculadora(5, 0, '^'), 1)
        self.assertEqual(calculadora(4, 0.5, '^'), 2)

    def test_operacao_invalida(self):
        self.assertIsNone(calculadora(5, 3, '%'))

    def test_valores_nao_numericos(self):
        self.assertIsNone(calculadora('a', 3, '+'))
        self.assertIsNone(calculadora(5, 'b', '+'))
        self.assertIsNone(calculadora('a', 'b', '+'))

if __name__ == '__main__':
    unittest.main()
