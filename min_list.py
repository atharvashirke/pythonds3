def find_min_n(input):
    """
    Given a list, find the minimum value. O(n)
    solution
    """
    min = input[0]
    for number in input:
        if min > number:
            min = number
    return min

def find_min_n2(input):
    """
    Given a list, find the minimum value. O(n^2)
    solution
    """
    min = input[0]
    for number in input:
        issmallest = True
        for other_number in input:
            if number > other_number:
                issmallest = False
        if issmallest:
            min = number
    return min

def main():
    list = [3, 7 , 51, 84]
    print(find_min_n(list))

main()
