#!/usr/local/bin/python3

from brain_games.cli import run
from brain_games.games import gcd


def main():
    run(gcd)


if __name__ == '__main__':
    main()
