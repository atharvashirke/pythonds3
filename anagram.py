def is_anagram(string1, string2):
    """
    Checks if string 1 and string 2 are anagrams of each other
    O(n) solution
    Returns a boolean
    """
    if len(string1) != len(string2):
        return False

    used_characters_1 = {}
    used_characters_2 = {}
    for char in string1:
        if char in used_characters_1:
            used_characters_1[char] = used_characters_1[char] + 1
        else:
            used_characters_1[char] = 1
    for char in string2:
        if char in used_characters_2:
            used_characters_2[char] = used_characters_2[char] + 1
        else:
            used_characters_2[char] = 1
    return used_characters_1 == used_characters_2

def main():
    s1 = "earth"
    s2 = "heart"
    print(is_anagram(s1, s2))

main()
