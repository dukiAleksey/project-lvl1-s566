import random
from fractions import gcd


DESCRIPTION = 'Find the greatest common divisor of given numbers.'
ATTEMPTS = 3


def stage():
    number1 = random.randrange(100)
    number2 = random.randrange(100)
    answer = gcd(number1, number2)
    return (f'Question: {number1} {number2}', answer)
