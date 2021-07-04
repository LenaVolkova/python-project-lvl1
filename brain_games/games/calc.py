import prompt
from random import randint


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print("What is the result of the expression?")
    return name


def ask_question():
    operand1 = randint(1, 100)
    operand2 = randint(1, 100)
    operator_number = randint(0, 2)
    operators = ('+', '-', '*')
    print('Question: {} {} {}'.format(operand1, operators[operator_num], operand2))
    if operator_number == 0:
        answer = operand1 + operand2
    elif operator_number == 1:
        answer = operand1 - operand2
    else:
        answer = operand1 * operand2
    return str(answer)
