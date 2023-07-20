from functools import reduce
from operator import mul


def factorial(x):
    return reduce(mul, range(1, x + 1))
