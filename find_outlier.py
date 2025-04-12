# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 14:32:31 2025

@author: Omnia Agabani
"""

def find_outlier(integers: list) -> (int, str):
    """
    Take an array numbers an check the outlier number

    Parameters
    ----------
    integers : list
        list of integers

    Returns
    -------
    (int, str)
        the outlier integer

    """
    odd = []
    even = []
    for num in integers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
            
    if len(even) == 1:
        return even[0]
    else:
        return odd[0]