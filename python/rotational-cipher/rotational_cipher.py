"""Rotational Cipher problem from exercism.io"""

import string

ALPHABET = list(string.ascii_lowercase)
DOUBLE_ALPHABET = ALPHABET + ALPHABET


def rotate(text, key):
    """Given a piece of text, return a version of it rotate, like on a
    ceasar cipher."""

    cipher_alphabet = DOUBLE_ALPHABET[key:(key + 26)]
    rotated = ''

    for char in text:
        if char.isalpha() is False:
            rotated += char
            continue

        address = ALPHABET.index(char.lower())
        new_char = cipher_alphabet[address]

        if char.isupper():
            rotated += new_char.upper()
        else:
            rotated += new_char

    return rotated
