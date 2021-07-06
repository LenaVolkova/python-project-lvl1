#!/usr/bin/env python3
from brain_games.games.games_engine import game
from brain_games.games.odd_even import make_question


def main():
    rules = "Answer \"yes\" if the number is even, otherwise answer \"no\"."
    game(rules, make_question)


if __name__ == '__main__':
    main()
