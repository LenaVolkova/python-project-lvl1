import random


RULES = "What is the result of the expression?"
MIN_NUMBER = 1
MAX_NUMBER = 100


def make_question():
    operand1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operand2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    sign = random.choice(['+', '-', '*'])
    question = '{} {} {}'.format(str(operand1), sign, str(operand2))
    answer = get_answer(operand1, sign, operand2)
    return (question, answer)


def get_answer(operand1, sign, operand2):
    if sign == '+':
        answer = operand1 + operand2
    elif sign == '-':
        answer = operand1 - operand2
    elif sign == '*':
        answer = operand1 * operand2
    else:
        return "Uknown operation"
    return str(answer)
