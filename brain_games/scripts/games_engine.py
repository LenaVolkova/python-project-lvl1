#!/usr/bin/env python3
import prompt


MAX_ROUNDS = 3


def run_game(rules, make_question):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(rules)
    count = 0
    while count < MAX_ROUNDS:
        question, correct_answer = make_question()
        print('Question: {}'.format(question))
        user_answer = prompt.string('Your answer: ')
        if correct_answer == user_answer:
            count += 1
            print("Correct!")
        else:
            count = MAX_ROUNDS
    if str(correct_answer) == user_answer:
        print('Congratulations, {}!'.format(name))
    else:
        print(
            f'\'{user_answer}\' is wrong answer ;(.'
            + f'Correct answer was \'{correct_answer}\'.')
        print('Let\'s try again, {}!'.format(name))
