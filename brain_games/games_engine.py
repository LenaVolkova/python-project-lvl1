#!/usr/bin/env python3
import prompt


MAX_ROUNDS = 3


def run_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(game.RULES)
    for count in range(0, MAX_ROUNDS):
        question, correct_answer = game.make_question()
        print('Question: {}'.format(question))
        user_answer = prompt.string('Your answer: ')
        if correct_answer == user_answer:
            print("Correct!")
        else:
            break
    if correct_answer == user_answer:
        print('Congratulations, {}!'.format(name))
    else:
        print(
            f'\'{user_answer}\' is wrong answer ;(.'
            + f'Correct answer was \'{correct_answer}\'.')
        print('Let\'s try again, {}!'.format(name))
