from deque import Deque

def palindrome_checker(input):
    """Checks if string is a palindrome. Returns boolean"""
    d1 = Deque()
    for char in input:
        d1.add_rear(char)
    while d1.size() > 1:
        front = d1.remove_front()
        rear = d1.remove_rear()
        if front != rear:
            return False
    return True

def main():
    word = "racecar"
    print(palindrome_checker(word))

main()
