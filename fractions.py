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

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

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

main()
