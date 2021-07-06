from random import randint


def make_question():
    number = randint(1, 100)
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    question = str(number)
    return (question, answer)
