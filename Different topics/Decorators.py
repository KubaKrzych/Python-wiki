"""
Decorators
As the name of the abstract might suggest it just decorates a function with another function.
Comes in handy, whenever we want to add extra functionality to our function without changing its body.

To describe decorators we will use a term wrapper. As it name may suggest it wraps around something. Let's suppose
we have a function, for example let's say that it just prints out a sum of given args.
But what if I would like to print out elements themselves, and also after printing out the sum, I would like to
calculate a square root of that sum and then print it out, BUT I also want to keep the function that just prints out the
sum of numbers. That's where the decorator shines, as it lets the original function to shine just by WRAPPING it with
the decorator functionality.
"""
import time
from random import randint


def my_decorator(function):

    def wrapper(*args):
        print("You passed in: {}".format([*args]))  # Before calling function
        sum = function(*args)
        print("Square root of the calculated sum is: ", sum ** (1 / 2))  # After calling function
        return function

    return wrapper


@my_decorator
def my_function(*args):
    print("Sum of these numbers is: ", sum([*args]))
    return sum([*args])


# res = my_function(1, 2, 4)
# print(res, "\n\n")
# res(1, 2)

# Below is a much more practical use of decorators. I will define two functions, and a decorator. Both functions will
# do the same thing, but one is more efficient than the other. I want to time both of them, without changing their body.


def time_function(function):

    def wrapper(*args):
        beg = time.time()
        result = function(*args)
        print(result)
        print(f"It took {time.time() - beg} seconds to run the function.")

    return wrapper


@time_function
def my_linear_find(x: float, elements: list):
    time.sleep(1)
    for i in elements:
        if i == x:
            return True
    return False


@time_function
def my_binary_find(x: int, items: list, start: int, end: int ):
    time.sleep(1)
    while start < end:
        mid = (end+start)//2
        if items[mid] < x:
            start = mid + 1
        elif items[mid] > x:
            end = mid - 1
        else:
            return True
    return x == items[mid]


items = sorted([randint(1, 1000) for i in range(3000000)])
my_binary_find(137, items, 0, len(items))
my_linear_find(137, items)

# Python also allows users to create decorator classes.


class Decorate(object):

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        print("This line comes from a class method and it run before running \"{}\".".format(self.function.__name__))
        self.function(*args, **kwargs)
        return self.function


@Decorate
def greet(name: str):
    print("Hello {}".format(name))


# greet("Kuba")
