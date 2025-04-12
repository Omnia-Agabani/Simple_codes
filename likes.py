# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 13:02:03 2025

@author: Omnia Agabani
"""

def likes(names: list) -> str:
    """
    The function will take the namees of the people who liked the post and
    return it as a sentence

    Parameters
    ----------
    names : list
        Names of people who liked the post

    Returns
    -------
    str
        text mentioning the people as a sentence

    """
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return names[0] + " likes this"
    elif len(names) == 2:
        return names[0] + " and " + names[1]+ " like this"
    elif len(names) == 3:
        return names[0] +", " + names[1]+ " and " + names[2]+ " like this"
    else:
        return names[0] +", " + names[1]+ " and " +str (len(names)-2) + " others like this"