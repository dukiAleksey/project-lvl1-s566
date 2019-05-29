import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
ATTEMPTS = 3


def stage():
    number = random.randrange(100)
    answer = 'yes' if is_prime(number) else 'no'
    return (f'Question: {number}', str(answer))


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if (num % i) == 0:
            return False
    return True
