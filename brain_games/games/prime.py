import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
ATTEMPTS = 3


def stage():
    number = random.randrange(100)
    answer = 'yes' if is_prime(number) else 'no'
    return (f'Question: {number}', answer)


def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False
