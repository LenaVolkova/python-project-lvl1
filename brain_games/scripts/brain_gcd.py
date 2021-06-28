#!/usr/bin/env python3
from brain_games.scripts.brain_even import game
from brain_games.games.gcd import welcome_user, ask_question


def main():
    game(welcome_user, ask_question)


if __name__ == '__main__':
    main()
