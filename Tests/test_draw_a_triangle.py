import unittest
from .draw_a_triangle import draw_a_triangle

class TestDrawTriangle(unittest.TestCase):
  def test_min_int(self):
    self.assertEqual (draw_a_triangle(0),'')
  def test_int(self):
    self.assertEqual (draw_a_triangle(10),'**********\n*********\n********\n*******\n******\n*****\n****\n***\n**\n*\n')
  def test_error_handling(self):
        """Test error handling for invalid inputs."""
        with self.assertRaises(AssertionError):
            draw_a_triangle('Omnia')  # string
        with self.assertRaises(AssertionError):
            draw_a_triangle([1,2,3])  # list
