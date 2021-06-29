import prompt
from random import randint


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print("Answer \"yes\" if the number is prime. Otherwise answer \"no\".")
    return name


def ask_question():
    random_number = randint(1, 500)
    print('Question: {}'.format(random_number))
    i = 2
    answer = 'yes'
    while i <= (random_number / 2):
        if random_number % i == 0:
            answer = 'no'
            i = random_number
        else:
            i += 1
    return answer
