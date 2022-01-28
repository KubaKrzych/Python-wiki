class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


class TwoWayNode(Node):
    def __init__(self, value, next, previous = None):
        super().__init__(value, next)
        self.previous = previous


class LinkedList:
    """
    A linked list is a data structure much appreciated by data engineers. It is very efficient when it comes to
    inserting a value into a DS, because it does not reallocate the existing DS, but simply allocates memory
    for a new node and then correctly connects the node with the existing linked nodes.
    """
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        self.head = Node(value, self.head)

    def insert_at_end(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        itr = self.head
        while itr.next is not None:
            itr = itr.next

        itr.next = Node(value, None)
        return

    def insert_array(self, array):
        self.head = None
        for data in array:
            self.insert_at_end(data)

    def delete_at_index(self, index):
        if index < 0 or index > self.__len__():
            raise Exception("Invalid index.")
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next

    def insert_at_index(self, value, index):
        if index < 0 or index > self.__len__():
            raise Exception("Invalid index.")
        itr = self.head
        count = 0
        while itr:
            if count == index -1:
                new_node = Node(value, itr.next)
                itr.next = new_node
                break
            count += 1
            itr = itr.next
        return

    def insert_after_value(self, after_value, value):
        itr = self.head
        while itr:
            if itr.value == after_value:
                new_node = Node(value, itr.next)
                itr.next = new_node
                return
            itr = itr.next
        print("There is no node that stores {}.".format(after_value))
        return

    def remove_by_value(self, value):
        itr = self.head
        while itr.next:
            if itr.next.value == value:
                itr.next = itr.next.next
                return
            itr = itr.next
        print("There is no node that stores {}.".format(value))
        return

    def sum(self):
        result = 0
        itr = self.head
        while itr:
            result += itr.value
            itr = itr.next
        return result

    def __len__(self):
        itr = self.head
        count = 0
        while itr is not None:
            count += 1
            itr = itr.next
        return count

    def __str__(self):
        res = ""
        itr = self.head
        while itr is not None:
            res += "{} ---> ".format(itr.value)
            itr = itr.next
        return res


class TwoWayLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
        self.head = None

    def insert_at_beginning(self, value):
        if self.head is None:
            self.head = TwoWayNode(value, None, None)
            return
        new_node = TwoWayNode(value, self.head, None)
        self.head.previous = new_node
        self.head = new_node

    def insert_at_index(self, value, index):
        if index < 0 or index > self.__len__():
            raise Exception("Invalid index.")

        itr = self.head
        count = 0

        while itr:
            if count == index-1:
                new_node = TwoWayNode(value, itr.next, itr)
                itr.next.previous = new_node
                itr.next = new_node
                break

            itr = itr.next
            count += 1


if __name__ == '__main__':
    ll = TwoWayLinkedList()
    ll.insert_at_beginning(13)
    ll.insert_at_beginning(13264)
    ll.insert_at_beginning(345)
    ll.insert_at_index(777, 1)
    print(ll)
