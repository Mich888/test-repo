"""Tests for math operations module."""

import unittest
from math_operations import subtract


class TestSubtract(unittest.TestCase):
    """Test cases for the subtract function."""
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        self.assertEqual(subtract(5, 3), 2)
    
    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""
        self.assertEqual(subtract(-5, -3), -2)
    
    def test_subtract_with_zero(self):
        """Test subtracting with zero."""
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(subtract(0, 5), -5)
    
    def test_subtract_equal_numbers(self):
        """Test subtracting equal numbers."""
        self.assertEqual(subtract(5, 5), 0)
    
    def test_subtract_floats(self):
        """Test subtracting floating point numbers."""
        self.assertAlmostEqual(subtract(5.5, 2.3), 3.2)


if __name__ == '__main__':
    unittest.main()
