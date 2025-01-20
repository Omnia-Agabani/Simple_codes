"""
Test suite for ASCII code conversion functionality.

Test categories:
    - Standard cases
    - Edge case
    - Defensive cases

Created on 20/01/2025
Author: Omnia_Agabani
"""
import  unittest
from ascii_code import ascii_code

class TestAsciiCode(unittest.TestCase):
    """class test ASCII code conversion functionality."""
    #Edge case:
    def test_empty_string(self):
        """Test empty string"""
        self.assertEqual(ascii_code(''),[])
    def test_whitespace(self):
        """Test conversion of whitespace character."""
        self.assertEqual(ascii_code(' '), [32])
    def test_new_line (self):
        """Test conversion of new line character."""
        self.assertEqual(ascii_code('\n'), [10])
    def test_tab_character (self):
        """Test conversion of tab character."""
        self.assertEqual(ascii_code('\t'), [9])
             
    # Stander cases
    def test_capital_chars(self):
        """Test conversion of capital alphabetic characters."""
        self.assertEqual(ascii_code('A'), [65])
    def test_small_chars(self):
        """Test conversion of small alphabetic characters."""
        self.assertEqual(ascii_code('a'), [97])
    def test_words(self):
        """Test conversion of one word."""
        self.assertEqual(ascii_code('Omnia'), [79, 109, 110, 105, 97])
    def test_special_chars(self):
        """Test conversion of special characters."""
        self.assertEqual(ascii_code('!'), [33])
    def test_string_number(self):
        """Test conversion of numeric characters."""
        self.assertEqual(ascii_code('0'), [48])
    
    # Defensive cases
    def test_list_input(self):
        """Test error handling for list inputs."""
        with self.assertRaises(AssertionError):
            ascii_code([1,2,3])
    def test_integer(self):
        """Test error handling for integer inputs."""
        with self.assertRaises(AssertionError):
            ascii_code(10) 
