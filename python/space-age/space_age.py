"""
Exercism.ui problem set = spacage!

https://exercism.io/my/solutions/7e08cf5c963843f083dfca3a04d54acc
"""

DAYS_IN_EARTH_YEAR = 365.25
SECONDS_IN_EARTH_DAY = 86400  # 60 * 60 * 24

ORBITAL_PERIODS = {
    'MERCURY': 0.2408467,
    'VENUS': 0.61519726,
    'MARS': 1.8808158,
    'JUPITER': 11.862615,
    'SATURN': 29.447498,
    'URANUS': 84.016846,
    'NEPTUNE': 164.79132
}


# pylint: disable=too-few-public-methods
class SpaceAge(object):
    """
    Main class for the problem. :)
    """
    def __init__(self, seconds):
        self.seconds = seconds

    def earth_years(self):
        return (self.seconds / SECONDS_IN_EARTH_DAY) * DAYS_IN_EARTH_YEAR

    def __getattr__(self, attrname):
        planet = attrname[3:].upper()
        if planet in ORBITAL_PERIODS:
            factor = ORBITAL_PERIODS.get(planet)
            return lambda: self.earth_years() * factor

        raise NameError
