#!/usr/bin/env python3
from brain_games.odd_even import welcome_user, check_answer, ask_question


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    count = 0
    true_answer = True
    q_and_a = (0, 'yes')
    correct_answer = 'yes'
    while count < 3 and true_answer:
        q_and_a = ask_question()
        true_answer = check_answer(q_and_a)
        if true_answer:
            count += 1
            print("Correct!")
        else:
            if q_and_a[0] % 2 == 1:
                correct_answer = "'yes'"
            else:
                correct_answer = "'no'"
            print(
                f'\'{q_and_a[1]}\' is wrong answer ;(.'
                + f'Correct answer was {correct_answer}.')
            print('Let\'s try again, {}!'.format(name))
    if true_answer:
        print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
