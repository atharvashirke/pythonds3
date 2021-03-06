def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n

class Fraction:
    """ A class representing a fraction. Requires a numerator and denominator
        for construction."""

    def __init__(self, num, den):
        cmmn = gcd(num, den)
        self.num = num // cmmn
        self.den = den // cmmn

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __repr__(self):
        return f"Fraction({self.num},{self.den})"

    def __add__(self, other_fraction):
        if isinstance(other_fraction, Fraction):
            new_num = self.num * other_fraction.den + self.den * other_fraction.num
            new_den = self.den * other_fraction.den
            return Fraction(new_num, new_den)
        elif isinstance(other_fraction, int):
            return self.__add__(Fraction(other_fraction, 1))

    def __radd__(self, other_fraction):
        if isinstance(other_fraction, Fraction):
            new_num = self.num * other_fraction.den + self.den * other_fraction.num
            new_den = self.den * other_fraction.den
            return Fraction(new_num, new_den)
        elif isinstance(other_fraction, int):
            return self.__add__(Fraction(other_fraction, 1))

    def __iadd__(self, other_fraction):
        if isinstance(other_fraction, Fraction):
            new_num = self.num * other_fraction.den + self.den * other_fraction.num
            new_den = self.den * other_fraction.den
            self.num, self.den = new_num, new_den
            return self
        elif isinstance(other_fraction, int):
            return self.__iadd__(Fraction(other_fraction, 1))

    def __sub__(self, other_fraction):
        new_num = self.num * other_fraction.den - self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __mul__(self, other_fraction):
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other_fraction):
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num
        return Fraction(new_num, new_den)

    def __gt__(self, other_fraction):
        self_new_num = self.num * other_fraction.den
        other_new_num = other_fraction.num * self.den
        return self_new_num > other_new_num

    def __ge__(self, other_fraction):
        self_new_num = self.num * other_fraction.den
        other_new_num = other_fraction.num * self.den
        return self_new_num >= other_new_num

    def __lt__(self, other_fraction):
        return not self.__gt__(other_fraction)

    def __le__(self, other_fraction):
        self_new_num = self.num * other_fraction.den
        other_new_num = other_fraction.num * self.den
        return self_new_num <= other_new_num

    def __ne__(self, other_fraction):
        self_new_num = self.num * other_fraction.den
        other_new_num = other_fraction.num * self.den
        return self_new_num != other_new_num

    def getnum(self):
        return self.num

    def getden(self):
        return self.den


def main():
    f1 = Fraction(1, 2)
    print(f1)
    print(f1.getnum())
    print(f1.getden())
    f2 = Fraction(3, 4)
    print(f1 + f2)
    print(f2 - f1)
    print(f1 * f2)
    print(f2 / f1)
    print(f1 > f2)
    f3 = Fraction(3, 4)
    print(f2 >= f3)
    print(f1 < f2)
    print(f2 <= f3)
    print(f1 != f3)
    f4 = Fraction(1, -2)
    print(f4)
    print(f4 > f1)
    print(1 + f1)
    print(f1 + 1)
    f1 += 2
    print(f1)
    print(repr(f1))

main()
