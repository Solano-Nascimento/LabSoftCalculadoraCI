import unittest
from calculadora import calcular

class TestCalcular(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(calcular("5 + 3"), 8)
        self.assertEqual(calcular("-5 + 3"), -2)
        self.assertEqual(calcular("5.5 + 2.5"), 8.0)
        self.assertEqual(calcular("10 + 5"), 15)

    def test_subtracao(self):
        self.assertEqual(calcular("5 - 3"), 2)
        self.assertEqual(calcular("-5 - 3"), -8)
        self.assertEqual(calcular("5.5 - 2.5"), 3.0)
        self.assertEqual(calcular("10 - 5"), 5)

    def test_multiplicacao(self):
        self.assertEqual(calcular("5 * 3"), 15)
        self.assertEqual(calcular("-5 * 3"), -15)
        self.assertEqual(calcular("5.5 * 2"), 11.0)
        self.assertEqual(calcular(" 10 * 5 "), 50)

    def test_divisao(self):
        self.assertEqual(calcular("6 / 3"), 2)
        self.assertEqual(calcular("-6 / 3"), -2)
        self.assertEqual(calcular("5 / 2"), 2.5)
        self.assertEqual(calcular(" 10 / 5 "), 2)

    def test_divisao_por_zero(self):
        self.assertIsNone(calcular("5 / 0"))

    def test_potenciacao(self):
        self.assertEqual(calcular("2 ^ 3"), 8)
        self.assertEqual(calcular("5 ^ 0"), 1)
        self.assertEqual(calcular("4 ^ 0.5"), 2)
        self.assertIsNone(calcular("0 ^ 0"))

    def test_expressoes_invalidas(self):
        self.assertIsNone(calcular("5 % 3"))
        self.assertIsNone(calcular("a + 5"))
        self.assertIsNone(calcular("5 + b"))
        self.assertIsNone(calcular("cinco + tres"))
        self.assertIsNone(calcular("5+"))
        self.assertIsNone(calcular("+5"))
        self.assertIsNone(calcular("5 5 + 3"))

    def test_espacamento_variado(self):
        self.assertEqual(calcular("5+3"), 8)
        self.assertEqual(calcular("   5   +    3   "), 8)
        self.assertEqual(calcular("-10.5-2.5"), -13.0)

if __name__ == '__main__':
    unittest.main()
