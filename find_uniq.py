# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 20:39:24 2025

@author: Omnia Agabani
"""

def find_uniq(arr: list) -> int:
    """
    There is an array with some numbers. All numbers are equal except for one.
    Try to find it!

    Parameters
    ----------
    arr : list
        array with some numbers, all numbers are equal except for one.

    Returns
    -------
    int
        Diffrent number

    """
    counter = {}
    for num in arr:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1
            
    for number in arr:
        if counter[number] == 1:
            return number