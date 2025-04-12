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
    """
    assert isinstance(text, str), "input must be a string"
    c = []
    for i in text:
        c.append(ord(i))        
    return c
