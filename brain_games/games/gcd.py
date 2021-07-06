from random import randint


def evklid_algorithm(num1, num2):
    if (num1 <= num2) and (num2 % num1 == 0):
        return num1
    while num1 != num2:
        if num1 < num2:
            min = num1
            diff = num2 - min
        else:
            min = num2
            diff = num1 - min
        num1 = min
        num2 = diff
    return num1


def make_question():
    num1 = randint(1, 100)
    num2 = randint(1, 200)
    question = str(num1) + ' ' + str(num2)
    answer = str(evklid_algorithm(num1, num2))
    return (question, answer)
