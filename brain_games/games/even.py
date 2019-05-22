import random


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'
ATTEMPTS = 3


def stage():
    number = random.randrange(20)
    answer = 'yes' if number % 2 == 0 else 'no'
    return (f'Question: {number}', answer)
