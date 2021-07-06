from random import randint, choice


def make_question():
    operand1 = randint(1, 100)
    operand2 = randint(1, 100)
    oper = choice(['+', '-', '*'])
    question = str(operand1) + ' ' + oper + ' ' + str(operand2)
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
