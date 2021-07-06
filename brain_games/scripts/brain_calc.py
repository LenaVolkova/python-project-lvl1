#!/usr/bin/env python3
from brain_games.games.games_engine import game
from brain_games.games.calc import make_question


def main():
    rules_string = "What is the result of the expression?"
    game(rules_string, make_question)


if __name__ == '__main__':
    main()
