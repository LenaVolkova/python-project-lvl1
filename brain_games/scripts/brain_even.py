#!/usr/bin/env python3
from brain_games.games.odd_even import welcome_user, get_answer
from brain_games.games.odd_even import ask_question, bye_user


MAX_COUNT = 3


def game(welcome_user, ask_question, get_answer, bye_user):
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
    game(welcome_user, ask_question, get_answer, bye_user)


if __name__ == '__main__':
    main()
