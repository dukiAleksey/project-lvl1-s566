import random


DESCRIPTION = 'What number is missing in the progression?'
ATTEMPTS = 3


def stage():
    p_len = random.randint(8, 11)
    p_step = random.randint(1, 10)
    p_start = random.randint(1, 10)
    progression = list(range(p_start, p_len * p_step, p_step))
    answer = random.choice(progression)
    progression = ['..' if x == answer else x for x in progression ]
    progression_string = " ".join(str(x) for x in progression)
    return (f'Question: {progression_string}', str(answer))
