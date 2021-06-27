import prompt
from random import randint


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def ask_question():
    random_number = randint(1, 100)
    print('Question: {}'.format(random_number))
    if random_number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return answer


def get_answer():
    answer = prompt.string('Your answer: ')
    return answer
