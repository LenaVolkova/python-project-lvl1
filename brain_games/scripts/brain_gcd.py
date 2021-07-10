#!/usr/bin/env python3
from brain_games.scripts.games_engine import run_game
from brain_games.games.gcd import make_question, RULES


def main():
    run_game(RULES, make_question)


if __name__ == '__main__':
    main()
