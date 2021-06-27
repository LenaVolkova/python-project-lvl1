#!/usr/bin/env python3
from brain_games.scripts.brain_even import game
from brain_games.games.calc import welcome_user, ask_question
from brain_games.games.calc import get_answer, bye_user


def main():
    game(welcome_user, ask_question, get_answer, bye_user)


if __name__ == '__main__':
    main()
