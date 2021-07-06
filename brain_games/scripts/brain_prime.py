#!/usr/bin/env python3
from brain_games.games.games_engine import game
from brain_games.games.prime import make_question


def main():
    rules = "Answer \"yes\" if the number is prime. Otherwise answer \"no\"."
    game(rules, make_question)


if __name__ == '__main__':
    main()
