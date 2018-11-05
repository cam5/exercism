"""exercism.io rational-numbers problem"""
from __future__ import division


class Rational(object):
    """
    Class representing a rational number.
    """
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        """
        The sum of two rational numbers r1 = a1/b1 and r2 = a2/b2
        is r1 + r2 =
           a1/b1 + a2/b2 =
           (a1 * b2 + a2 * b1) / (b1 * b2).
        """
        if not isinstance(other, Rational):
            raise Exception("Not comparing two rational numbers!")

        return Rational(
            (self.numer * other.denom + other.numer + self.denom),
            (self.denom * other.denom)
        )

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __abs__(self):
        pass

    def __pow__(self, power):
        pass

    def __rpow__(self, base):
        pass
