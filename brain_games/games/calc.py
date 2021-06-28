import prompt
from random import randint


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print("What is the result of the expression?")
    return name


def ask_question():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    num3 = randint(0, 2)
    operator = ('+', '-', '*')
    print('Question: {} {} {}'.format(num1, operator[num3], num2))
    if num3 == 0:
        answer = num1 + num2
    elif num3 == 1:
        answer = num1 - num2
    else:
        answer = num1 * num2
    return str(answer)
