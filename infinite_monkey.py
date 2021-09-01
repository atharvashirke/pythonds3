import random

sentence = "methinks it is like a weasel"

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

#input desired string length
def random_string(n):
    output = [
    while n > 0:
        output.append(random.choice(alphabet))
        n = n - 1
    return output

def score_sentence(sentence, original):
    max_score = len(original)
    score = 0
    for i in range(0, max_score):
        if (sentence[i] == original[i]):
            score = score + 1
    return score/max_score

monkey_sentence = []
count = 0
high_score = 0
best_sentence = []

while monkey_sentence != sentence:
    if count % 1000 == 0:
        print("".join(best_sentence) + " | similarity score: " + str(high_score))
    monkey_sentence = random_string(28)
    if score_sentence(monkey_sentence, sentence) > high_score:
        high_score = score_sentence(monkey_sentence, sentence)
        best_sentence = monkey_sentence
    count = count + 1

print("The monkeys took " + count + " tries to write shakespeare")
