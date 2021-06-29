import prompt
from random import randint


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print("What number is missing in the progression?")
    return name


def ask_question():
    member = randint(0, 100)
    step = randint(1, 10)
    size = randint(5, 10)
    missing_number = randint(0, size - 1)
    question_str = ''
    i = 0
    while i < size:
        if i == missing_number:
            question_str = ''.join([question_str, ' ..'])
        else:
            question_str = ' '.join([question_str, str(step * i + member)])
        i += 1
    print('Question: ' + question_str)
    answer = member + missing_number * step
    return str(answer)
