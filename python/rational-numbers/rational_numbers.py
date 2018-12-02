"""exercism.io rational-numbers problem"""
from __future__ import division
from math import gcd


class Rational(object):
    """
    Class representing a rational number.
    """
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

        """
        If the denominator is negative, don't represent it that way...
        flip 'em
        """
        if (0 > denom):
            self.numer = numer * -1
            self.denom = abs(denom)

        if self.numer == 0:
            self.denom = 1

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        """
        `r1 = a1/b1` and `r2 = a2/b2`
        is
        `r1 + r2 = a1/b1 + a2/b2 = (a1 * b2 + a2 * b1) / (b1 * b2)`.
        """
        if not isinstance(other, Rational):
            raise Exception("Not comparing two rational numbers!")

        ret_numer = self.numer * other.denom + other.numer * self.denom
        ret_denom = (self.denom * other.denom)

        if self.denom == other.denom:
            ret_denom = self.denom

        return Rational(ret_numer, ret_denom)

    def __sub__(self, other):
        """
        `r1 = a1/b1` and `r2 = a2/b2`
        is
        `r1 - r2 = a1/b1 - a2/b2 = (a1 * b2 - a2 * b1) / (b1 * b2)`.

        """
        if not isinstance(other, Rational):
            raise Exception("Not comparing two rational numbers!")

        ret_numer = self.numer * other.denom - other.numer * self.denom
        ret_denom = (self.denom * other.denom)

        if self.denom == other.denom:
            ret_denom = self.denom

        return Rational(ret_numer, ret_denom)

    def __mul__(self, other):
        """
        `r1 = a1/b1` and `r2 = a2/b2`
        is
        `r1 * r2 = (a1 * a2) / (b1 * b2)`.
        """
        if not isinstance(other, Rational):
            raise Exception("Not comparing two rational numbers!")

        if (other.denom == 1 and other.numer == 1):
            return self

        if (0 == self.numer or 0 == other.numer):
            return Rational(0, 1)

        numer = self.numer * self.denom
        denom = other.numer * other.denom
        greatest = gcd(numer, denom)

        return Rational(numer / greatest, denom / greatest)

    def __truediv__(self, other):
        """
        See https://stackoverflow.com/q/29155829, it seems like this deserves
        better understanding.
        """
        if not isinstance(other, Rational):
            raise Exception("Not comparing two rational numbers!")

        """
        Dividing a rational number `r1 = a1/b1`
                        by another `r2 = a2/b2`
        is `r1 / r2 = (a1 * b2) / (a2 * b1)`
        (if `a2 * b1` is not zero.)
        """
        if (other.denom == 1 and other.numer == 1):
            return self

        if ((self.denom * other.numer) != 0):
            numer = self.numer * other.denom
            denom = self.denom * other.numer

            return Rational(numer, denom)

    def __abs__(self):
        """
        Return the "absolute" value of the object.
        i.e. the absolute value of -1 is 1.
        """
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        pass

    def __rpow__(self, base):
        pass
