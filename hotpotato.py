from queue import Queue

def hotpotato(names, num):
    """
    Given a list of names, simulate a game of hot potato, returning
    the name of the winner. Num represents the number of passes in
    a round until someone is eliminated.
    """
    circle = Queue()
    for name in names:
        circle.enqueue(name)
    while circle.size() > 1:
        for i in range(num):
            circle.enqueue(circle.dequeue())
        circle.dequeue()
    return circle.dequeue()

def main():
    names = ["Mark", "Matt", "John", "Jason", "Kim", "Nash"]
    print(hotpotato(names, 7))

main()
