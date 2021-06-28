#!/usr/bin/env python3
from brain_games.games.odd_even import welcome_user
from brain_games.games.odd_even import ask_question
import prompt


MAX_COUNT = 3


def get_answer():
    answer = prompt.string('Your answer: ')
    return answer


def bye_user(correct_answer, user_answer, name):
    if str(correct_answer) == user_answer:
        print('Congratulations, {}!'.format(name))
    else:
        print(
            f'\'{user_answer}\' is wrong answer ;(.'
            + f'Correct answer was \'{correct_answer}\'.')
        print('Let\'s try again, {}!'.format(name))


def game(welcome_user, ask_question):
    print("Welcome to the Brain Games!")
    name = welcome_user()
    count = 0
    while count < MAX_COUNT:
        correct_answer = ask_question()
        user_answer = get_answer()
        if correct_answer == user_answer:
            count += 1
            print("Correct!")
        else:
            count = MAX_COUNT
    bye_user(correct_answer, user_answer, name)


def main():
    game(welcome_user, ask_question)


if __name__ == '__main__':
    main()
