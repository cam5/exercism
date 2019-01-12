"""exercism.io rational-numbers problem"""
try:
    from math import gcd
except ImportError:
    from fractions import gcd


def gcdize(rational):
    """
    Given a rational number, find its lowest-common-denominator, and also
    divide the numerator by it.

    Ex. rather than 5/10, return 1/2, or Rational(1, 2)
    """
    if not isinstance(rational, Rational):
        raise Exception("Can only greatest-common-denominatorize Rational")

    gcd_denom = gcd(rational.numer, rational.denom)

    return Rational((rational.numer / gcd_denom), (rational.denom / gcd_denom))


class Rational(object):
    """
    Class representing a rational number.
    """
    def __init__(self, numer, denom):
        self.numer = int(numer)
        self.denom = int(denom)

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
        gcd_self = gcdize(self)
        gcd_other = gcdize(other)

        return (gcd_self.numer == gcd_other.numer
                and gcd_self.denom == gcd_other.denom)

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

        numer = self.numer * other.numer
        denom = self.denom * other.denom
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
        """
        Return the rational number to the power of something (exponents).
        self ^ power

        Just recursively multiply factors X number of times.
        """
        if power > 1:
            product = self
            for _ in list(range(1, power)):
                product = product * self

            return product
        elif power == 0:
            """
            Good explanation of the to-the-power-of-0 rule
            here: https://is.gd/7gTSlB
            """
            return Rational(1, 1)
        else:
            return self

    def __rpow__(self, base):
        if (self.numer < 0):
            """
            I put this into wolfram alpha, and it said to represent it as
            1 / base to power of the positive version of the fraction.

            https://www.wolframalpha.com/input/?i=9%5E-0.5
            """
            return 1 / (base ** Rational(abs(self.numer), abs(self.denom)))

        return base ** (float(self.numer) / float(self.denom))
