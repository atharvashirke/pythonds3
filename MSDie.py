import random

class MSDie:
    """
    A Multisided Die

    Instance Variables:
        current_value
        num_sides
    """

    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()

    def __str__(self):
        return str(self.current_value)

    def __repr__(self):
        return f"MSDie({self.num_sides} : {self.current_value})"

    def roll(self):
        self.current_value = random.randint(1, self.num_sides + 1)
        return self.current_value

def main():
    d6 = MSDie(6)
    print(d6)
    print(repr(d6))

main()
