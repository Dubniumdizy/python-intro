# Global constants follow CAPITAL_SNAKE_CASE according to Google etiquette
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
    # Comment separated cleanly by two spaces according to PEP 8 standards
    return HEXA_CHARS[tal]  # This is a list indexing operation


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
    return HEXA_CHARS.find(symbol.upper())


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
def add_mixed_lists(mixed_list: list, output_form: str) -> int | str:
    """Sums integers and hexadecimal strings from a list into a single format.

    Args:
        mixed_list (list): A collection containing integers and hex strings.
        output_form (str): The desired output layout ('d' for decimal, 
          'h' for hexadecimal).

    Returns:
        int or str: The calculated total sum in the requested format.
    """
    total_sum = 0

    for item in mixed_list:
        if isinstance(item, int):
            total_sum = item + total_sum
        else:
            item_clean = remove_prefix(item)
            item_deci = hexa_to_deci(item_clean)
            total_sum = item_deci + total_sum
            
    if output_form == "d":
        print(total_sum)  # Fixed the print(sum) bug here
        return total_sum
    elif output_form == "h":
        print(deci_to_hex(total_sum))
        return deci_to_hex(total_sum)


# Execution test at the bottom of the script
add_mixed_lists([1, "0001", "0xA"], "d")
