"""
Easier approach would be just import 'heapq'.
Heap indexes:
    Left child index: 2*index + 1
    Right child index: 2*index +2
    Parent: (index-1)/2
"""


class BinaryHeap:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def parent(self, index):
        return self.storage[self.get_parent_index(index)]

    def is_full(self):
        return self.capacity == self.size

    def is_empty(self):
        return self.size == 0

    def swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp

    def insert(self, data):
        if self.is_full():
            raise "Storage is full"
        self.storage[self.size] = data
        self.size += 1
        self.recursive_heap(self.size - 1)

    def recursive_heap(self, index):
        if self.get_parent_index(index) >= 0 and self.parent(index) > self.storage[index]:
            self.swap(index, self.get_parent_index(index))
            self.recursive_heap(self.get_parent_index(index))

    def iterative_heap(self):
        index = self.size - 1
        while self.get_parent_index(index) >= 0 and self.parent(index) > self.storage[index]:
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    def remove_min(self):
        if self.is_empty():
            raise "Storage is empty."
        index = self.size - 1
        self.swap(0, index)
        self.storage[index] = None
        self.recursive_heap(self.get_parent_index(index))
        self.size -= 1

    @staticmethod
    def get_parent_index(index):
        return (index-1)//2

    @staticmethod
    def get_left_child_index(index):
        return 2*index + 1

    @staticmethod
    def get_right_child_index(index):
        return 2*index + 2


if __name__ == "__main__":
    heap = BinaryHeap(7)
    heap.insert(20)
    heap.insert(10)
    heap.insert(8)
    heap.insert(5)
    heap.insert(0)
    print(heap.storage)