"""Allergies Problem from exercism.io"""

ALLERGY_LIST = (
    'eggs',
    'peanuts',
    'shellfish',
    'strawberries',
    'tomatoes',
    'chocolate',
    'pollen',
    'cats',
)


def dec_to_bin(decimal):
    """Represent a decimal as binary, and strip off the 0b at front."""
    return bin(decimal)[2:]


class Allergies(object):
    """class to test allergies"""

    def __init__(self, score):
        self._score = score

    def is_allergic_to(self, item):
        """Returns boolean indicating if allergic to supplied allergy string"""
        return item in self.lst

    @property
    def lst(self):
        """Lists the allergies that this Allergies class is allergic to"""
        allergies = []

        """List bits in same order as ALLERGY_LIST, and cast ints so they're
        truthy or falsy"""
        bit_list = [int(b) for b in reversed(dec_to_bin(self._score))]
        position = 0

        for bit in bit_list:
            if bit:
                try:
                    allergies.append(ALLERGY_LIST[position])
                except IndexError:
                    pass
            position += 1

        return allergies
