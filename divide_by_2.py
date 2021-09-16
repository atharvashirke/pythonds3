from stack import Stack

def divide_by_2(num):
    """
    Converts base 10 integer into binary representation
    """
    output = Stack()
    binary = []
    while num > 0:
        remainder = num % 2
        output.push(remainder)
        num = num // 2
    while not output.is_empty():
        binary.append(output.pop())
    return "".join([str(x) for x in binary])

def change_base(base, num):
    """
    Converts base 10 integer into desired base representation
    """
    remainders = Stack()
    output = ""
    digits = "0123456789ABCDEF"
    while num > 0:
        remainder = num % base
        remainders.push(remainder)
        num = num // base
    while not remainders.is_empty():
        output = output + str(digits[remainders.pop()])
    return output

def main():
    number = 256
    print(divide_by_2(number))
    print(change_base(16, number))

main()
