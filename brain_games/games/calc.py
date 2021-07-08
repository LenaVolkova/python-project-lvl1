import random


RULES = "What is the result of the expression?"
MIN_NUMBER = 1
MAX_NUMBER = 100


def make_question():
    operand1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operand2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    oper = random.choice(['+', '-', '*'])
    question = '{} {} {}'.format(str(operand1), oper, str(operand2))
    answer = get_answer(operand1, oper, operand2)
    return (question, answer)


def get_answer(operand1, operator, operand2):
    if operator == '+':
        answer = operand1 + operand2
    elif operator == '-':
        answer = operand1 - operand2
    else:
        answer = operand1 * operand2
    return str(answer)
