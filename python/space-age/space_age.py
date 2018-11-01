"""
Exercism.ui problem set = spacage!

https://exercism.io/my/solutions/7e08cf5c963843f083dfca3a04d54acc
"""

"""
Orbital periods, relative to earth.

Ex. In the time it takes Mercury to make one full revolution of the sun, Earth
will only have orbited 0.2408467 of the way.
"""
ORBITAL_PERIODS = {
    'EARTH': 1,
    'MERCURY': 0.2408467,
    'VENUS': 0.61519726,
    'MARS': 1.8808158,
    'JUPITER': 11.862615,
    'SATURN': 29.447498,
    'URANUS': 84.016846,
    'NEPTUNE': 164.79132
}


class SpaceAge(object):
    """
    Handles data and calculations concerning the age of a person on different
    planets, given a number of 'earth seconds'.
    """
    def __init__(self, seconds):
        self.seconds = seconds

    def earth_years(self):
        """
        Calculate the number of earth revolutions that a person would have been
        present for, given a number of seconds.
        """
        days_in_earth_year = 365.25
        seconds_in_earth_day = 86400  # 60 * 60 * 24

        return self.seconds / (seconds_in_earth_day * days_in_earth_year)

    def __getattr__(self, attrname):
        """
        Returns a function calculating age in {planet} years, where the planet
        is known, else, a regular getattr call.
        """
        planet = attrname[3:].upper()
        if planet in ORBITAL_PERIODS:
            factor = ORBITAL_PERIODS.get(planet)
            return lambda: round(self.earth_years() / factor, 2)

        return getattr(self, attrname)
