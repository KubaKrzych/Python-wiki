"""
Deque is much more efficient than an array, mainly because when your data does not fully fit in
previously allocated memory then python allocates new memory two times the size, and then copies the
data to the second array.
"""

from collections import deque
import threading
import time

class Queue:
    def __init__(self):
        self.buffer = deque()

    def queue(self, value):

        self.buffer.appendleft(value)

    def dequeue(self):
        return self.buffer.pop()

    def __len__(self):
        return len(self.buffer)

    def __str__(self):
        return str(self.buffer)


class Restaurant(Queue):
    def __init__(self):
        super().__init__()

    def serve_order(self):
        if self.__len__() == 0:
            return
        time.sleep(2)
        return self.dequeue()

    def place_order(self, value):
        time.sleep(0.5)
        self.queue(value)

if __name__ == "__main__":
    q = Restaurant()
    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    for i in orders:
        t1 = threading.Thread(target=q.place_order, args=(i,))
        t2 = threading.Thread(target=q.serve_order)
    t1.start()
    t2.start()

    t1.join()
    t2.join()