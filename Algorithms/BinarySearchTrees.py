"""
Every node has at most two child nodes. Great to store values in as in python's sets. It stores only one instance
of the value. Its great power comes from its speed to check whether the value is stored as its time complexity i O(logN)
E.g.
         15
   12          27
7    14      20   88
            23
"""


class BinaryNode():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def search(self, data):
        if self.data == data:
            return True
        elif self.data > data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        else:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def insert(self, data):
        if self.data == data:
            return
        elif self.data > data:
            if self.left:
                return self.left.insert(data)
            self.left = BinaryNode(data)
        else:
            if self.right:
                return self.right.insert(data)
            self.right = BinaryNode(data)

    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.data

    def find_max(self):
        if self.right:
            return self.right.find_min()
        return self.data

    def get_min(self):
        head = self
        while self.left:
            head = self.left
        return head

    def get_max(self):
        head = self
        while self.right:
            head = self.right
        return head

    def inorder(self):
        elements = []
        if self.left:
            elements += self.left.inorder()
        elements.append(self.data)
        if self.right:
            elements += self.right.inorder()
        return elements

    def preorder(self):
        elements = [self.data]
        if self.left:
            elements += self.left.preorder()
        if self.right:
            elements += self.right.preorder()
        return elements

    def postorder(self):
        elements = []
        if self.left:
            elements += self.left.postorder()
        if self.right:
            elements += self.right.postorder()
        elements.append(self.data)
        return elements

    def delete(self, data):
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
                return self
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
                return self
        else:
            if self.left and self.right:
                self.data = self.left.find_max()
                self.left = self.left.delete(self.data) # 21
                return self
            elif self.left:
                return self.left
            elif self.right:
                return self.right


if __name__ == "__main__":
    els = [15, 8, 24, 5, 19, 30, 21]
    root = BinaryNode(els[0])
    for i in els[1:]:
        root.insert(i)
    print(root.preorder())
    root.delete(19)
    print(root.preorder())
