"""Level 1: Lambda, map/filter/reduce, recursion, args/kwargs, iterators, generators, decorators, and context managers."""

from functools import reduce
from contextlib import contextmanager

square = lambda x: x * x
print("Lambda:", square(6))

numbers = [1, 2, 3, 4, 5]
print("Map:", list(map(lambda x: x * 2, numbers)))
print("Filter:", list(filter(lambda x: x % 2 == 0, numbers)))
print("Reduce:", reduce(lambda acc, x: acc + x, numbers, 0))


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))


def show_args(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)


show_args(1, 2, 3, name="Asha", role="student")

class NumberIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        self.current += 1
        return self.current


iterator = NumberIterator(3)
print("Iterator:", list(iterator))


def number_generator(limit):
    for value in range(limit):
        yield value


print("Generator:", list(number_generator(4)))


def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        return result

    return wrapper


@decorator
def greet(name):
    return f"Hello {name}"


print(greet("Asha"))


@contextmanager
def sample_context():
    print("Entering context")
    try:
        yield
    finally:
        print("Exiting context")


with sample_context():
    print("Inside context")
