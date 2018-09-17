"""Allergies Problem from exercism.io"""

ALLERGY_LIST = {
    'eggs': 1,
    'peanuts': 2,
    'shellfish': 4,
    'strawberries': 8,
    'tomatoes': 16,
    'chocolate': 32,
    'pollen': 64,
    'cats': 128,
}

class Allergies(object):
    """class to test allergies"""

    def __init__(self, score):
        self._score = score

    def is_allergic_to(self, item):
        """Returns boolean indicating if allergic to supplied allergy string"""
        return item in self.lst

    @property
    def lst(self):
        """Lists the things that this Allergies list contains"""
        score = self._score
        allergies = []

        for allergy, value in sorted(
                ALLERGY_LIST.iteritems(),
                key=lambda (k, v): (v, k),
                reverse=True
        ):
            # Ex. 34, 32
            if score >= value:
                allergies.append(allergy)

        return allergies
