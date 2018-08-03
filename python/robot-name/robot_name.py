"""Robot Name exercise for Python track of exercism.io"""

import random
import string


class Robot():
    """Robot whose name is unique at each instantiation"""

    name = ''

    def __init__(self):
        self.name = self.generate_name()

    @staticmethod
    def generate_name():
        """Picks a random name"""
        random.seed()

        letters = ''
        number = random.randint(100, 999)

        for _ in range(2):
            letters += random.choice(string.ascii_uppercase)

        return '{}{}'.format(letters, number)

    def reset(self):
        """Assigns a new name to the robot."""
        self.name = self.generate_name()
