""" Program to test """
import unittest
import findline_equation

class TestCalc(unittest.TestCase):
    """Test class for parameter testing"""

    def test_find_line_from_two_coordinates(self):
        """Method to test different parameters"""
        self.assertEqual(findline_equation.find_line_from_two_coordinates(
            ['2','5','3','5']), "1 y = 5")
        self.assertEqual(findline_equation.find_line_from_two_coordinates(
            ['2.5','0','2','7']), "-7 x + -1/2 y = -35/2")
        self.assertEqual(findline_equation.find_line_from_two_coordinates(
            ['8','5.3','6.3','5.0']), "3/10 x + -17/10 y = -661/100")
        self.assertEqual(findline_equation.find_line_from_two_coordinates(
            ['24','3.4','30','5.4']), "-2 x + 6 y = -138/5")
        self.assertEqual(findline_equation.find_line_from_two_coordinates(
            ['1.4','5.4','3.77','5.54']), "-7/50 x + 237/100 y = 6301/500")

if __name__ == '__main__':
    unittest.main()
