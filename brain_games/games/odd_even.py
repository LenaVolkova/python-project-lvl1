from random import randint


RULES = "Answer \"yes\" if the number is even, otherwise answer \"no\"."
MIN_NUMBER = 1
MAX_NUMBER = 100


def make_question():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    question = str(number)
    return (question, answer)
