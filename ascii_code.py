#!/user/bin/env python3
# *-* coding: utf-8 *-*
"""
    This module contains a function that converts a string to a list of ASCII codes.
    It takes a string as input and returns a list of ASCII codes for each character in the string.
    
    Created on 20/01/2025
    Author: Omnia_Agabani
    """
def ascii_code(text: str) -> list:
    """
    Converts a string to a list of ASCII codes
    for each character in the string.
    
    Parameters:
        text (str): The input string to be converted.
    
    Returns:
        list: A list of ASCII codes for each character
        in the input string.
    
    Raises:
        AssertionError: If the input is not a string.
    
    Example:
        >>> ascii_code("hello")
        [104, 101, 108, 108, 111]
    """
    assert isinstance(text, str), "input must be a string"
    c = []
    for i in text:
        c.append(ord(i))        
    return c
