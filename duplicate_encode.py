# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 13:46:19 2025

@author: Omnia Agabani
"""

def duplicate_encode(word: str) -> str:
    """
    convert a string to a new string where each character in the new string is
    "(" if that character appears only once in the original string, or ")"
    if that character appears more than once in the original string.

    Parameters
    ----------
    word : str
        Orignal text

    Returns
    -------
    str
        Encoded text

    """
    Word = word.lower()
    counter = {}
    new = ""
    for letter in list(Word):
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
            
    for letter in list(Word):
        if counter[letter] == 1:
            new += "("
        else:
            new += ")"
            
    return new