import unittest
import operations

class Test(unittest.TestCase):

    def setUp(self):
        self.operations = operations

    def test_add(self):
        self.assertEqual(self.operations.add(3, 2), 5)
        self.assertEqual(self.operations.add(-1, -1), -2)
        self.assertEqual(self.operations.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.operations.subtract(3, 2), 1)
        self.assertEqual(self.operations.subtract(-1, -1), 0)
        self.assertEqual(self.operations.subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(self.operations.multiply(3, 2), 6)
        self.assertEqual(self.operations.multiply(-1, 2), -2)
        self.assertEqual(self.operations.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(self.operations.divide(6, 2), 3)
        self.assertEqual(self.operations.divide(-4, 2), -2)
        with self.assertRaises(ValueError):
            self.operations.divide(5, 0)

    def test_modulus(self):
        self.assertEqual(self.operations.modulus(6.2, 2), 0.2)
        self.assertEqual(self.operations.modulus(5, 2), 1)
        with self.assertRaises(ValueError):
            self.operations.modulus(5, 0)

    def test_power(self):
        self.assertEqual(self.operations.power(2, 3), 8)
        self.assertEqual(self.operations.power(5, 0), 1)
        self.assertEqual(self.operations.power(0, 5), 0)

if __name__ == "__main__":
    unittest.main()
