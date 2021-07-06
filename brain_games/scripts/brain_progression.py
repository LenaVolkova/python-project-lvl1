#!/usr/bin/env python3
from brain_games.games.games_engine import game
from brain_games.games.progression import make_question


def main():
    rules_string = "What number is missing in the progression?"
    game(rules_string, make_question)


if __name__ == '__main__':
    main()
