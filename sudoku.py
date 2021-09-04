class Square:

    def __init__(self, number = None):
        self.num = number

    def __repr__(self):
        return f"Square({self.num})"

    def __str__(self):
        return f"|{self.num}|"

    def get_value():
        return self.num

    def set_num(new_num):
        if self.num == None:
            self.num = new_num
        else:
            raise RuntimeError("Cannot Fill Pre-Filled Square")

class Grid:

    def __init__(self):
        

def main():
    s1 = Square(1)
    print(s1)

main()
