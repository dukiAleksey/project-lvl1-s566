import random

from brain_games.cli import greet
from brain_games.cli import ask


ATTEMPTS = 3


def main():
    name = greet()
    for a in range(ATTEMPTS):
        number = random.randint(1, 20)
        correct_answer = 'yes' if number % 2 == 0 else 'no'
        answer = ask(f'Question: {number}')
        if answer in correct_answer:
            print(f'Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. " \
                f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return


if __name__ == '__main__':
    main()