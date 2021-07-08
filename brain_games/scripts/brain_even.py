#!/usr/bin/env python3
from brain_games.scripts.games_engine import game
from brain_games.games.odd_even import make_question, RULES


def main():
    game(RULES, make_question)


if __name__ == '__main__':
    main()
