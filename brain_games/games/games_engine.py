#!/usr/bin/env python3
import prompt


MAX_COUNT = 3


def welcome_user(rules):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(rules)
    return name


def bye_user(correct_answer, user_answer, name):
    if str(correct_answer) == user_answer:
        print('Congratulations, {}!'.format(name))
    else:
        print(
            f'\'{user_answer}\' is wrong answer ;(.'
            + f'Correct answer was \'{correct_answer}\'.')
        print('Let\'s try again, {}!'.format(name))


def game(rules, make_question):
    name = welcome_user(rules)
    count = 0
    while count < MAX_COUNT:
        question_and_answer = make_question()
        print('Question: ' + question_and_answer[0])
        user_answer = prompt.string('Your answer: ')
        if question_and_answer[1] == user_answer:
            count += 1
            print("Correct!")
        else:
            count = MAX_COUNT
    bye_user(question_and_answer[1], user_answer, name)
