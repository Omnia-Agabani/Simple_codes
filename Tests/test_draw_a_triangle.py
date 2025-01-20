#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for Draw triangle function.

Test categories:
    - Standard cases
    - Edge cases
    - Defensive tests

Created on 20/10/2025
Author: Omnia_Agabani
"""
import unittest
from draw_a_triangle import draw_a_triangle
class TestDrawTriangle(unittest.TestCase):
  """ Test class for Draw triangle function."""
  
  #Edge cases:
  def test_Zero(self):
    """ Test for zero input."""
    self.assertEqual (draw_a_triangle(0),'')
  def test_One(self):
    """ Test for one input."""
    self.assertEqual (draw_a_triangle(1),'*\n')
    
  #Standard cases:
  def test_small_int(self):
    """Test for small input"""
    self.assertEqual (draw_a_triangle(5),'*****\n****\n***\n**\n*\n')
  def test_large_int(self):
    """Test for large  input"""
    self.assertEqual (draw_a_triangle(10),'**********\n*********\n********\n*******\n******\n*****\n****\n***\n**\n*\n')
  
  # Defensive cases:
  def test_string_input(self):
        """Test error handling for string inputs."""
        with self.assertRaises(AssertionError):
            draw_a_triangle('Omnia') 
  def test_list_input(self):
        """Test error handling for List inputs.""" 
        with self.assertRaises(AssertionError):
            draw_a_triangle([1,2,3])
  def test_negative_input(self):
        """Test error handling for negative inputs.""" 
        with self.assertRaises(AssertionError):
            draw_a_triangle(-7)
