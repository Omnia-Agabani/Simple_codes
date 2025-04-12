# -*- coding: utf-8 -*-
"""      
Created on Sat Apr 12 12:17:10 2025

@author: Omnia Agabani
"""
def GCD (x,y)-> int:
    """
    Find the greatest common divisor of two positive integers
    

    Parameters
    x, y(int): positive integer we want to find the greatest
               common divisor for

    Returns
        integer which is the greatest common divisor
        
    Tests:
        >>> GCD(48, 18)
        6
        >>> GCD(17, 5)
        1
        >>> GCD(0, 8)
        8
        >>> GCD(144, 36)
        36
        >>> GCD(1071, 462)
        21
    """
    if x == 0 or x == y:
        return y
    elif y == 0:
        return x
    elif x > y:
        return GCD(x-y, y)
    else: 
        return GCD (y-x,x)