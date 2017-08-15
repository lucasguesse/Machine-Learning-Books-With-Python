import unittest
import numpy as np
from numpy_recreate import Array1D


class TestAdd(unittest.TestCase):

    def test_basic_equality(self):
        data = [1, 2, 3, 4]
        a = np.array(data)
        b = Array1D(data)
        self.assertEqual(a.tolist(), b.data)

        a = np.random.rand(100)
        b = Array1D(a.tolist())
        self.assertEqual(a.tolist(), b.data)

    def test_arithmetic_scalar(self):
        a = np.random.rand(100)
        b = Array1D(a.tolist())

        a1 = a + 5
        b1 = b + 5
        self.assertEqual(a1.tolist(), b1.data)

        a1 = a - 10.987
        b1 = b - 10.987
        self.assertEqual(a1.tolist(), b1.data)

        a1 = a * 10.987
        b1 = b * 10.987
        self.assertEqual(a1.tolist(), b1.data)

        a1 = a / -9.8
        b1 = b / -9.8
        self.assertEqual(a1.tolist(), b1.data)

        a1 = a ** 2
        b1 = b ** 2
        self.assertEqual(a1.tolist(), b1.data)

        a1 = (a * 100) // 3
        b1 = (b * 100) // 3
        self.assertEqual(a1.tolist(), b1.data)

        a1 = (a * 100) % 87
        b1 = (b * 100) % 87
        self.assertEqual(a1.tolist(), b1.data)

        a1 = 10 + a
        b1 = 10 + b
        self.assertEqual(a1.tolist(), b1.data)

        a1 = -98 - a
        b1 = -98 - b
        self.assertEqual(a1.tolist(), b1.data)

        a1 = 17 * a
        b1 = 17 * b
        self.assertEqual(a1.tolist(), b1.data)

        a1 = a / -9.8
        b1 = b / -9.8
        self.assertEqual(a1.tolist(), b1.data)

        a1 = 3 ** a
        b1 = 3 ** b
        self.assertEqual(a1.tolist(), b1.data)

        a1 = 10 // a
        b1 = 10 // b
        self.assertEqual(a1.tolist(), b1.data)

        a1 = 87 % a
        b1 = 87 % b
        self.assertEqual(a1.tolist(), b1.data)

    def test_arithmetic_scalar_int(self):
        a = np.random.randint(1, 10, 100)
        b = Array1D(a.tolist())

        a1 = a + 5
        b1 = b + 5
        self.assertEqual(a1.tolist(), b1.data)

        a1 = a - 10.987
        b1 = b - 10.987
        self.assertEqual(a1.tolist(), b1.data)

        a1 = a * 10.987
        b1 = b * 10.987
        self.assertEqual(a1.tolist(), b1.data)

        a1 = a / -9.8
        b1 = b / -9.8
        self.assertEqual(a1.tolist(), b1.data)

        a1 = a ** 2
        b1 = b ** 2
        self.assertEqual(a1.tolist(), b1.data)

        a1 = (a * 100) // 3
        b1 = (b * 100) // 3
        self.assertEqual(a1.tolist(), b1.data)

        a1 = (a * 100) % 87
        b1 = (b * 100) % 87
        self.assertEqual(a1.tolist(), b1.data)

        a1 = 10 + a
        b1 = 10 + b
        self.assertEqual(a1.tolist(), b1.data)

        a1 = -98 - a
        b1 = -98 - b
        self.assertEqual(a1.tolist(), b1.data)

        a1 = 17 * a
        b1 = 17 * b
        self.assertEqual(a1.tolist(), b1.data)

        a1 = a / -9.8
        b1 = b / -9.8
        self.assertEqual(a1.tolist(), b1.data)

        a1 = 3 ** a
        b1 = 3 ** b
        self.assertEqual(a1.tolist(), b1.data)

        a1 = 10 // a
        b1 = 10 // b
        self.assertEqual(a1.tolist(), b1.data)

        a1 = 87 % a
        b1 = 87 % b
        self.assertEqual(a1.tolist(), b1.data)

    def test_logical_scalar(self):
        a = np.random.rand(100)
        b = Array1D(a.tolist())
        a1 = a > .4
        b1 = b > .4
        self.assertEqual(a1.tolist(), b1.data)

        a1 = a < .8
        b1 = b < .8
        self.assertEqual(a1.tolist(), b1.data)

        a = np.random.randint(0, 10, 100)
        b = Array1D(a.tolist())
        a1 = a >= 4
        b1 = b >= 4
        self.assertEqual(a1.tolist(), b1.data)

        a1 = a <= 6
        b1 = b <= 6
        self.assertEqual(a1.tolist(), b1.data)

        a1 = a == 4
        b1 = b == 4
        self.assertEqual(a1.tolist(), b1.data)

        a1 = a != 2
        b1 = b != 2
        self.assertEqual(a1.tolist(), b1.data)


if __name__ == '__main__':
    unittest.main()