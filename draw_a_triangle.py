#!/user/bin/env python3
# *-* coding: utf-8 *-*
"""
  This code draw a triangle with a number of stars in each line
  and a number of lines in the triangle.
  The first line has Num stars,
  the second line has Num-1 stars, and so on..
  
  Created on 20/01/2025
  Author: Omnia_Agabani
  """
def draw_a_triangle (Num : int):
  """
  function draw a triangle

  parameters:
  Num: number of stars in the first line

  returns:
  Strings representing the triangle
  
  Raises:
  AssertionError:
  If Num is not an integer
  If Num is less than or equal to 0
  
  Examples:
  --------
  >>> draw_a_triangle(4)
  ****
  ***
  **
  *
  
  >>> draw_a_triangle('d')
  "Num must be an integer"
  
  >>> draw_a_triangle(-5)
  "Num must be positive"
  
  """
  assert isinstance(Num, int), "Num must be an integer"
  assert Num >= 0 , "Num must be positive"
  c = ''

  for i in range(Num, 0, -1):
      c += ('*' * i)+'\n'

  return c
