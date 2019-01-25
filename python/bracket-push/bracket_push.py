"""bracket-push module for exercism.io"""

OPENING_CHARS = ('[', '{', '(')
CLOSING_CHARS = (']', '}', ')')
CHAR_MAP = {'[': ']', '{': '}', '(': ')'}


def is_paired(input_string):
    """
    tests if a string has matching brackets.

    (will not catch quoted parens.)
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

    well_ordered = True

    if input_string != '' and input_string[0] in CLOSING_CHARS:
        well_ordered = False

    opened_parens = []

    for char in input_string:
        if char in OPENING_CHARS:
            opened_parens.append(char)

        # If We've logged opening parens, and now we're at a closing one...
        if char in CLOSING_CHARS and opened_parens:
            # Make sure that it matches the most-recently opened paren.
            if char != CHAR_MAP.get(opened_parens[-1], False):
                well_ordered = False

            # Move cursor to next most recent
            opened_parens.pop()

    return balanced and well_ordered
