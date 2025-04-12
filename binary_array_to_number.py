# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 14:55:15 2025

@author: Omnia Agabani
"""

def binary_array_to_number(arr: list) -> int:
    """
    Given an array of ones and zeroes, convert the equivalent binary value to an integer.

    Parameters
    ----------
    arr : list
        array of ones and zeroes want to convert

    Returns
    -------
    int
        the equivelent value of the array

    """
    binary = ""
    for i in arr:
        binary += str(i)
    return int(binary,2)