import unittest
from calc import *

def setUpModule():
    print('Start the testing module')


class TestCalculator(unittest.TestCase):

   # Create an instance of the calculator 
   @classmethod
   def setUpClass(self):
      print('Set up class')
      self.calc = Calculator()

   #Test cases
   def test_add(self):
      self.assertEqual(self.calc.add(2, 7), 9, msg="Passed")
      self.assertEqual(self.calc.add(-5, 5), 0, msg="Passed")
      self.assertEqual(self.calc.add(-7, -5), -12, msg="Passed")

   def test_subtract(self):
      self.assertEqual(self.calc.subtract(2, 7), -5, msg="Passed")
      self.assertEqual(self.calc.subtract(-5, 6), -11, msg="Passed")
      self.assertEqual(self.calc.subtract(7, -5), 12, msg="Passed")

   def test_multiply(self):
      self.assertEqual(self.calc.multiply(2, 7), 14, msg="Passed")
      self.assertEqual(self.calc.multiply(-5, 6), -30, msg="Passed") 
      self.assertEqual(self.calc.multiply(-1, 1), -1, msg="Passed")
      self.assertEqual(self.calc.multiply(-1, -1), 1, msg="Passed")  

   def test_divide(self):
      
      self.assertEqual(self.calc.divide(10, 5), 2, msg="Passed")
      self.assertEqual(self.calc.divide(-1, 1), -1, msg="Passed")
      self.assertEqual(self.calc.divide(-1, -1), 1, msg="Passed")
      self.assertEqual(self.calc.divide(5, 2), 2.5, msg="Passed")

   def test_interger_divide(self):
      
      self.assertEqual(self.calc.integer_divide(10, 5), 2, msg="Passed")
      self.assertEqual(self.calc.integer_divide(-1, 1), -1, msg="Passed")
      self.assertEqual(self.calc.integer_divide(-1, -1), 1, msg="Passed")
      self.assertEqual(self.calc.integer_divide(5, 2), 2, msg="Passed")  

   def test_power(self):
      
      self.assertEqual(self.calc.power(10, 2), 100, msg="Passed")
      self.assertEqual(self.calc.power(-1, 1), -1, msg="Passed")
      self.assertEqual(self.calc.power(2, -2), 0.25, msg="Passed")

   def test_factorial(self):
      
      self.assertEqual(self.calc.factorial(1), 1, msg="Passed")
      self.assertEqual(self.calc.factorial(0), 1, msg="Passed")
      self.assertEqual(self.calc.factorial(5), 120, msg="Passed")

def tearDownModule():
    print('End the testing module')


if __name__ == '__main__':
   unittest.main()



