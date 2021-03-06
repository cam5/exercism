"""Isbn Verifier Exercise from exercism.io"""


def verify(isbn):
    """Given an input string, validate wether or not it is an ISBN"""
    char_list = [d for d in list(isbn) if d != '-']

    # don't allow lists of less than 10 digits
    if len(char_list) < 10:
        return False

    # Replace our check digit if it's an X
    if char_list[-1] == 'X':
        char_list[-1] = 10

    # If there's something other than a number at this point, it's invalid.
    for char in char_list:
        if isinstance(char, str) and char.isdigit() is False:
            return False

    factor = 10
    val = 0

    digit_list = [int(d) for d in char_list]

    for digit in digit_list:
        val = val + digit * factor
        factor = factor - 1

    return val % 11 == 0
