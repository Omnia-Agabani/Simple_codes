# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 14:09:55 2025

@author: Omnia Agabani
"""

def is_square(n: int) -> bool:
    """
    Given an integral number, determine if it's a square number

    Parameters
    ----------
    n : int
        the tested number

    Returns
    -------
    bool
        Is the number is square?

    """
    
    if n < 0:
        return False        
    root = int(n ** 0.5)
    return root * root == n