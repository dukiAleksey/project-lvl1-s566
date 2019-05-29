import random


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'
ATTEMPTS = 3


def stage():
    number = random.randrange(20)
    answer = 'yes' if not number % 2 else 'no'
    return (f'Question: {number}', str(answer))
