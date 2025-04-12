# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 15:04:08 2025

@author: Omnia Agabani
"""

def longest_consec(strarr : list, k: int) -> str:
    """
    

    Parameters
    ----------
    strarr : list
    k : int
        Concatenate the consecutive strings of strarr by k

    Returns
    -------
    str
        first longest string consisting of k consecutive strings taken in the array.

    """
    n = len(strarr)
    
    if n == 0 or k > n or k <= 0:
        return ""
    
    longest = ""
    for i in range(n - k + 1): 
        check = ""
        for j in range(k): 
            check += strarr[i + j]
        if len(check) > len(longest):
            longest = check
            
    return longest