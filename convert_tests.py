import unittest
import convert

class Tests(unittest.TestCase):

    def test_str_to_float_1(self):
        result = convert.str_to_float("Water")
        expected = None
        self.assertEqual(expected, result)

    def test_str_to_float_2(self):
        result = convert.str_to_float("0.769")
        expected = 0.769
        self.assertAlmostEqual(expected, result)

if __name__ == "__main__":
    unittest.main()