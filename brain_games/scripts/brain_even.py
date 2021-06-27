#!/usr/bin/env python3
from brain_games.odd_even import welcome_user, get_answer, ask_question


MAX_COUNT = 3


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    count = 0
    true_answer = True
    correct_answer = 'yes'
    user_answer = 'yes'
    while count < MAX_COUNT and true_answer:
        correct_answer = ask_question()
        user_answer = get_answer()
        if correct_answer == user_answer:
            count += 1
            print("Correct!")
        else:
            true_answer = False
            print(
                f'\'{user_answer}\' is wrong answer ;(.'
                + f'Correct answer was \'{correct_answer}\'.')
            print('Let\'s try again, {}!'.format(name))
    if true_answer:
        print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
