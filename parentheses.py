from stack import Stack

def par_checker(string):
    """
    Given a string, check if parentheses are balanced
    """
    openings = Stack()
    for char in string:
        if char == '(':
            openings.push('(')
        elif char == ")":
            try:
                openings.pop()
            except IndexError:
                print("Unbalanced")
                return False
    return openings.is_empty()

def par_checker_adv(string):
    """
    Given a string, check if parentheses are balanced
    Includes support for multiple bracket types
    """
    brackets = {'}':'{', ')':'(', ']':'['}
    openings = Stack()
    for char in string:
        if char in brackets.values():
            openings.push(char)
        elif char in brackets.keys():
            if brackets[char] == openings.peek():
                openings.pop()
            else:
                return False
    return openings.is_empty()


def main():
    example = "(()()()())"
    example2 = "((((((())"
    example3 = "{ { ( [ ] [ ] ) } ( ) }"
    example4 = "( ( ( ) ] ) )"
    print(par_checker_adv(example4))

main()
