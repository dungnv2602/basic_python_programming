import unittest
import calc


class TestCalculate(unittest.TestCase):

    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        # test raise exception
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
