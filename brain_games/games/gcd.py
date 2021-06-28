import prompt
from random import randint


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print("Find the greatest common divisor of given numbers.")
    return name


def evklid(num1, num2):
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


def ask_question():
    num1 = randint(1, 100)
    num2 = randint(1, 200)
    print('Question: {} {}'.format(num1, num2))
    answer = evklid(num1, num2)
    return str(answer)
