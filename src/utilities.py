import time
from random import random, uniform


def gen(min: int = 0, max: int = 1) -> int:
    ''' Generates random integer from [min, max] range (defaults to [0, 1]). '''
    return int(random() * (max - min + 1) + min)


def genf(min: float = -1, max: float = 1) -> float:
    ''' Generates random float from [min, max] (defaults to [-1, 1]). '''
    return uniform(min, max)


def with_timer(fun, repeat: int = 1):
    ''' 
    Wrapper that prints time spent on function execution. Returns function
    wrapped with timer functionality, function to get time spend, and 
    array of results in ms.
    '''
    times = []

    def inner(*args, **kwargs):
        for i in range(repeat):
            print(f"Running {i}-th iteration.", end="\r")

            start = time.time()
            result = fun(*args, **kwargs)
            end = time.time()

            times.append((end - start) * 1000 )

        inner.__setattr__('times', times)
        return result

    return inner, lambda: sum(times), times
