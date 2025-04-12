import  unittest
from .ascii_code import ascii_code

class TestAsciiCode(unittest.TestCase):
    """Test suite for ASCII code conversion functionality."""
    def test_basic_chars(self):
        """Test conversion of basic alphabetic characters."""
        self.assertEqual(ascii_code('A'), [65])
        self.assertEqual(ascii_code('Z'), [90])
        self.assertEqual(ascii_code('a'), [97])
        self.assertEqual(ascii_code('z'), [122])
    def test_words(self):
        """Test conversion of basic alphabetic characters."""
        self.assertEqual(ascii_code('Omnia'), [79, 109, 110, 105, 97])
        self.assertEqual(ascii_code('Agabani'), [65, 103, 97, 98, 97, 110, 105])
    def test_whitespace(self):
        """Test conversion of whitespace characters."""
        self.assertEqual(ascii_code(''),[]) # empty string
        self.assertEqual(ascii_code(' '), [32])  # space
        self.assertEqual(ascii_code('\t'), [9])  # tab
        self.assertEqual(ascii_code('\n'), [10])# newline
    
    def test_special_chars(self):
        """Test conversion of special characters."""
        self.assertEqual(ascii_code('!'), [33])
        self.assertEqual(ascii_code('@'), [64])
        self.assertEqual(ascii_code('#'), [35])
        self.assertEqual(ascii_code('$'), [36])
    
    def test_numbers(self):
        """Test conversion of numeric characters."""
        self.assertEqual(ascii_code('0'), [48])
        self.assertEqual(ascii_code('9'), [57])
    
    def test_special_chars_input(self):
        """Test handling of special character inputs."""
        self.assertEqual(ascii_code('*'), [42])
        self.assertEqual(ascii_code('^'), [94])
        self.assertEqual(ascii_code('&'), [38])
    
    def test_error_handling(self):
        """Test error handling for invalid inputs."""
        with self.assertRaises(AssertionError):
            ascii_code([1,2,3])# list
        with self.assertRaises(AssertionError):
            ascii_code(10)  # Integer
