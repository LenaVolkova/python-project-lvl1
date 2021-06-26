import prompt
from random import randint


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def ask_question():
    random_number = randint(1, 100)
    answer = prompt.string('Question: ' + str(random_number) + '\n')
    return (random_number, answer)


def check_answer(question_and_answer):
    if question_and_answer[0] % 2 == 0 and question_and_answer[1] == 'yes':
        return True
    elif question_and_answer[0] % 2 == 1 and question_and_answer[1] == 'no':
        return True
    else:
        return False
