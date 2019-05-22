import random

from brain_games.cli import greet
from brain_games.cli import ask


DESCRIPTION = 'What number is missing in the progression?'
ATTEMPTS = 3


def stage():
    p_len = random.randint(8, 11)
    p_step = random.randint(1, 10)
    p_start = random.randint(1, 10)
    p_hidden = random.randrange(p_len - 1)
    print(p_len, p_step, p_start, p_hidden)
    progression = list(range(p_start, p_len * p_step, p_step))
    answer = progression[p_hidden]
    print(answer)
    progression[p_hidden] = '..'
    progression = " ".join(str(x) for x in progression)
    return (f'Question: {progression}', answer)