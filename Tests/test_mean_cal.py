import unittest
from .mean_cal import mean_cal

class TestMeanCal(unittest.TestCase):
  def test_min_list (self):
    """ empty list"""
    self.assertEqual(mean_cal([]),0)
  def test_list_of_int (self):
    """list of int"""
    self.assertEqual(mean_cal([5,10,15,20,10]), 12.0)
    
  def test_list_of_str (self):
    """list of string"""
    with self.assertRaises(AssertionError):
      mean_cal(['o','12','a'])
  def test_string (self):
    """Input string"""
    with self.assertRaises(AssertionError):
      mean_cal('o')
  