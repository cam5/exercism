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
    def allergy_vals(self):
        return sorted(ALLERGY_LIST.values())

    def remove_unknown_allergens(self, score):
        """Normalizes a score, such that nothing we know for sure as another
        allergen is calculated against."""
        highest_known_allergy = self.allergy_vals[-1]
        next_known_allergy = highest_known_allergy * 2

        while score > highest_known_allergy and score > next_known_allergy:
            """Keep calculating allergens until we exceed the score"""

            while score > next_known_allergy:
                # Go up by 1 step
                next_known_allergy = next_known_allergy * 2

            # Back up by 1 step
            next_known_allergy = next_known_allergy / 2
            score -= next_known_allergy

        return score

    @property
    def lst(self):
        """Lists the things that this Allergies list contains"""
        score = self.remove_unknown_allergens(self._score)
        allergies = []

        for allergy, value in sorted(
                ALLERGY_LIST.iteritems(),
                key=lambda (k, v): (v, k),
                reverse=True
        ):
            # Ex. 34, 32
            if score >= value:
                allergies.append(allergy)
                score -= value

        return allergies
