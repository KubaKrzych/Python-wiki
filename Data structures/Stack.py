"""
Last in first out,
E.g. ctrl+z or stacking functions in any programming language.
Comes in handy whenever the user has access only to the last stored value .
"""

from collections import deque

class Stack:
    def __init__(self):
        self.buffer = deque()

    def get(self):
        if self.__len__() == 0:
            return None
        return self.buffer.pop()

    def put(self, value):
        self.buffer.append(value)

    def peek(self):
        return self.buffer[-1]

    def __len__(self):
        return len(self.buffer)


def reverse_string(string: str, stack: Stack):
    i = 0
    while i < len(string):
        stack.put(string[i])
        i += 1
    res = ""
    while len(stack):
        res += stack.get()
    return res

s = Stack()
imie = "kuba"
imie = reverse_string(imie, s)
print(imie)