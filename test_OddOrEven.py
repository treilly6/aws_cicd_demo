import unittest
from OddEven import OddOrEven
from Errors import OddEvenError

class TestOddOrEven(unittest.TestCase):

    def test_even_number(self):
        test_number = OddOrEven(10)
        self.assertEqual(test_number.parity, 'EVEN', 'Incorrect parity value')

    def test_odd_number(self):
        test_number = OddOrEven(9)
        self.assertEqual(test_number.parity, 'ODD', 'Incorrect parity value')

    def test_incorrect_types(self):
        with self.assertRaises(OddEvenError):
            OddOrEven(8.0)
        
        with self.assertRaises(OddEvenError):
            OddOrEven('asdgasdg')

        with self.assertRaises(OddEvenError):
            OddOrEven(None)

        with self.assertRaises(OddEvenError):
            OddOrEven([])

        with self.assertRaises(OddEvenError):
            OddOrEven({})

        with self.assertRaises(OddEvenError):
            OddOrEven(90)

if __name__ == "__main__":
    unittest.main()