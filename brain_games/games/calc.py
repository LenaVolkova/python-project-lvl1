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
    operator_num = randint(0, 2)
    oper = ('+', '-', '*')
    print('Question: {} {} {}'.format(operand1, oper[operator_num], operand2))
    if operator_num == 0:
        answer = operand1 + operand2
    elif operator_num == 1:
        answer = operand1 - operand2
    else:
        answer = operand1 * operand2
    return str(answer)
