#!/usr/bin/env python3
from brain_games.games.games_engine import game
from brain_games.games.gcd import make_question


def main():
    rules_string = "Find the greatest common divisor of given numbers."
    game(rules_string, make_question)


if __name__ == '__main__':
    main()
