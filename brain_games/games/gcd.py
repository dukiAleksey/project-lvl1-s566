import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'
ATTEMPTS = 3


def stage():
    number1 = random.randrange(100)
    number2 = random.randrange(100)
    answer = get_gcd(number1, number2)
    return (f'Question: {number1} {number2}', str(answer))


def get_gcd(a, b):
    if not b:
        return a
    else:
        return get_gcd(b, a % b)
