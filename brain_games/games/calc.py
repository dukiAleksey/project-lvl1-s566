import operator
import random

DESCRIPTION = 'What is the result of the expression?'
ATTEMPTS = 3


def stage():
    number1 = random.randrange(100)
    number2 = random.randrange(100)
    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}
    oper_sign = random.choice(list(ops.keys()))
    answer = ops[oper_sign](number1, number2)
    return (f'Question: {number1} {oper_sign} {number2}', answer)
