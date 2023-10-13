def input_matematika():
    print("=" * 25)
    print("operasi matematika")
    print(" 1. jumlah \t [+]")
    print(" 2. jumlah \t [-]")
    print(" 3. jumlah \t [*]")
    print("=" * 25)
   
operasi = input("pilih operasi (1/2/3): ")


print("=" * 25)

def add (a, b):
    if operasi == '1':
        return a + b

def subtract(a, b):
    if operasi == '2':
        return a - b

def multiply(a, b):
    if operasi == '3':
        return a * b


def power(base, exponent):
    return base ** exponent

import unittest

class TestCalculatorFunctions(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(3, 3), 6)

    def test_subtraction(self):
        self.assertEqual(subtract(4, 3), 1)

    def test_multiplication(self):
        self.assertEqual(multiply(2, 5), 10)

    def test_power(self):
        self.assertEqual(power(3, 3), 27)

if __name__ == "__main__":
    unittest.main()