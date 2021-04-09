from random import random


def gen(max: int = 1) -> int:
    ''' Generates random number from [0, max] range. '''
    return int(random() * max)
