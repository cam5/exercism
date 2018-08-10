"""bracket-push module for exercism"""

OPENING_CHARS = ('[', '{', '(')
CLOSING_CHARS = (']', '}', ')')
CHAR_MAP = {'[': ']', '{': '}', '(': ')'}


def is_paired(input_string):
    """
    tests if a string has matching brackets.

    The supplied test does not check for wether or not the brackets are
    inverse.
    i.e. ][ - will technically pass this test for the moment.
    """

    input_array = list(input_string)
    opening_counts = {}
    closing_counts = {}

    for char in OPENING_CHARS:
        opening_counts[char] = input_array.count(char)

    for char in CLOSING_CHARS:
        closing_counts[char] = input_array.count(char)

    balanced = True

    for char in OPENING_CHARS:
        if opening_counts[char] != closing_counts[CHAR_MAP[char]]:
            balanced = False

    print(opening_counts, closing_counts)

    return balanced
