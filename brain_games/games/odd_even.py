import prompt
from random import randint


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
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


def bye_user(correct_answer, user_answer, name):
    if correct_answer == user_answer:
        print('Congratulations, {}!'.format(name))
    else:
        print(
            f'\'{user_answer}\' is wrong answer ;(.'
            + f'Correct answer was \'{correct_answer}\'.')
        print('Let\'s try again, {}!'.format(name))
