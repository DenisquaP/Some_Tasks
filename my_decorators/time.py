from time import time


def func_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        end = time()
        return end - start, res
    return wrapper
