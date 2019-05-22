import random

from brain_games.cli import greet
from brain_games.cli import ask

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'
ATTEMPTS = 3


def stage():
    number = random.randrange(20)
    answer = 'yes' if number % 2 == 0 else 'no'

    # name = greet(DESCRIPTION)
    # correct_answers_counter = 0
    # for a in range(ATTEMPTS):
    #     number = random.randint(1, 20)
    #     answer = 'yes' if number % 2 == 0 else 'no'
    #     answer = ask()
    #     if answer == correct_answer:
    #         correct_answers_counter += 1
    #         print(f'Correct!')
    #     else:
    #         print(f"'{answer}' is wrong answer ;(. " \
    #             f"Correct answer was '{correct_answer}'")
    #         print(f"Let's try again, {name}!")
    #         return
    
    # if correct_answers_counter == ATTEMPTS:
    #     print(f'Congratulations, {name}!')
    
    return (f'Question: {number}', answer)