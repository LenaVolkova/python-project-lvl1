#!/usr/bin/env python3
import prompt


MAX_COUNT = 3


def game(rules, make_question):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(rules)
    count = 0
    while count < MAX_COUNT:
        question, correct_answer = make_question()
        print('Question: {}'.format(question))
        user_answer = prompt.string('Your answer: ')
        if correct_answer == user_answer:
            count += 1
            print("Correct!")
        else:
            count = MAX_COUNT
    if str(correct_answer) == user_answer:
        print('Congratulations, {}!'.format(name))
    else:
        print(
            f'\'{user_answer}\' is wrong answer ;(.'
            + f'Correct answer was \'{correct_answer}\'.')
        print('Let\'s try again, {}!'.format(name))
