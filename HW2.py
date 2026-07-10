"""Hexadecimal and Decimal Converter Laboratory Assignment.

This script provides utility functions to convert and manipulate hexadecimal 
and decimal numbers without using built-in conversion libraries.

1. Make hexa_chars a global variable
2. Add the comments from above
3. Use find()/index() in 1b. Python strings only allow you to look up items using integers
4. Hexa_to_deci lacks a return statment
5. Use two empty rows between global functions, classes, import to first function/class. 
Use one empty row between smaller logic like methods in a class, inside a function body
"""

# Global variables 
HEXA_CHARS = "0123456789ABCDEF"

# =============================================================================
# Uppgift 1a
# =============================================================================
def int_to_hexa_char(tal: int) -> str:
    """Converts an integer in the range 0-15 to its hexadecimal character.

    Args:
        tal (int): An integer value in the range 0 to 15.

    Returns:
        str: The corresponding single hexadecimal character.
    """
    return hexa_chars[tal] # This is a list indexing operation


# =============================================================================
# Uppgift 1b
# =============================================================================
def hexa_char_to_int(symbol: str) -> int:
    """Converts a single hexadecimal character to its corresponding integer.

    Args:
        symbol (str): A string character representing a hex digit (0-9, A-F).

    Returns:
        int: The corresponding integer value in the range 0 to 15.
    """
    # Using .find() as recommended in the assignment tips
    return hexa_chars.find(symbol.upper())


# =============================================================================
# Uppgift 2
# =============================================================================
def hexa_to_deci(hexa: str) -> int:
    """Converts a hexadecimal string (without prefix) to a decimal integer.

    Args:
        hexa (str): A string of hexadecimal characters without a prefix.

    Returns:
        int: The equivalent base-10 decimal integer value.

    Example: "1A" -> 26
    First: decimal_value = 0 * 16 + 1 = 1
    Second: decimal_value = 1 * 16 + 10 = 26

    965_dec = 3C5_hex -> (C=12)
    result = 0
    result = 0 * 16 + 3 = 3 (ental)
    result = 3 * 16 + 12 = 60 (tiotal)
    result = 60 * 16 + 5 = 965 (hundratal)

    """
    decimal_value = 0
    for char in hexa:
        decimal_value = (decimal_value * 16) + hexa_char_to_int(char)
    return decimal_value


# =============================================================================
# Uppgift 3
# =============================================================================
def deci_to_hex(deci: int) -> str:
    """Converts a decimal integer to a hexadecimal string representation.

    Args:
        deci (int): A base-10 decimal integer.

    Returns:
        str: The equivalent hexadecimal string representation.

    Example: 26 -> "1A"
    First: remainder = 26 % 16 = 10
    Second: remainder = 1 % 16 = 1
    """
    if deci == 0:
        return "0"
        
    hexa_string = ""
    while deci > 0:
        remainder = deci % 16
        hexa_string = int_to_hexa_char(remainder) + hexa_string
        deci = deci // 16
    return hexa_string


# =============================================================================
# Uppgift 4
# =============================================================================
def remove_prefix(hexa: str) -> str:
    """Removes '0x' prefix and leading zeros from a hexadecimal string.

    Args:
        hexa (str): A hexadecimal string which may contain a '0x' prefix 
          or leading zeros.

    Returns:
        str: A cleaned hexadecimal string with prefix and leading zeros stripped.
    
    Example: "0x0001A" -> "1A", "0x0000" -> "0", "1A" -> "1A"
    """
    if hexa.startswith("0x"):
        hexa = hexa[2:]
        
    # Use a while loop and slicing as recommended in the tips to strip leading zeros
    idx = 0
    while idx < len(hexa) and hexa[idx] == "0":
        idx += 1
        
    result = hexa[idx:]
    if result == "":
        return "0"
    return result


# =============================================================================
# Uppgift 5
# =============================================================================
def add_mixed_list(mixed_list: list, output_form: str) -> int | str:
    """Sums integers and hexadecimal strings from a list, returning the specified format.

    Args:
        mixed_list (list): A list containing integers and hexadecimal strings.
        output_form (str): The desired format of the output ('d' for decimal 
          integer, 'h' for hexadecimal string).

    Returns:
        int or str: The total sum calculated from the list elements in the 
          requested format type.

    Example: mixed_list = [10, "0x1A", 5], output_form = "d" -> returns 41
    """
    total = 0
    for item in mixed_list:
        if isinstance(item, int):
            total += item
        elif isinstance(item, str):
            clean_hex = remove_prefix(item)
            total += hexa_to_deci(clean_hex)
            
    if output_form == "d":
        return total
    elif output_form == "h":
        return deci_to_hex(total)
    
###############################################################

def add_mixed_lists (mixed_list, output_form):
    sum = 0

    for char in mixed_list:
        if isinstance(char, int):
            sum = char + sum
        else:
            char_clean = remove_prefix(char)
            char_deci = hexa_to_deci(char_clean)
            sum = char_deci + sum
           
    if output_form == "d":
        return sum
    elif output_form == "h":
        return deci_to_hexa(sum)

add_mixed_list([1,"0001","0xA"], "d")
print(sum)




# =============================================================================
# Uppgift 6a
# =============================================================================
def validate_hexa(string: str) -> bool:
    """Validates whether a given string is a valid hexadecimal representation.

    Args:
        string (str): The input text string to analyze for valid hex qualities.

    Returns:
        bool: True if the string evaluates to a valid hexadecimal format, 
          False otherwise.
    """
    if string == "":
        return False
        
    if string.startswith("0x"):
        string = string[2:]
        if string == "":
            return False
            
    valid_chars = "0123456789ABCDEFabcdef"
    for char in string:
        if valid_chars.find(char) == -1: # If char is not found in valid_chars, find() returns -1
            return False
    return True


# =============================================================================
# Uppgift 6b
# =============================================================================
def valid_hexa_list(string_list: list[str]) -> list[str]:
    """Filters a list of strings, returning a new list with only valid hex strings.

    Args:
        string_list (list): A collection of strings to check for validity.

    Returns:
        list: A separate, filtered list containing only elements that are 
          valid hexadecimal strings.
    """
    filtered_list = []
    for string in string_list:
        if validate_hexa(string):
            filtered_list.append(string)
    return filtered_list

if __name__ == "__main__":
    # Testing
    print(int_to_hexa_char(4))
    print(hexa_char_to_int("D"))


######################################################################################################################################################################


