class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.parent = None
        self.lastSearchDepth = 0

    def insert(self, value):
        if self.parent is None:
            self.parent = Node(value)

        else:
            parent = self.parent
            while True:
                if value > parent.value:
                    if parent.right is None:
                        parent.right = Node(value)
                        return
                    else:
                        parent = parent.right
                elif value < parent.value:
                    if parent.left is None:
                        parent.left = Node(value)
                        return
                    else:
                        parent = parent.left

    def fromArray(self, array):
        for value in array:
            self.insert(value)

    def search(self, value):
        item = self.parent
        originalLastSearchDepth = self.lastSearchDepth
        self.lastSearchDepth = 0

        while item is not None:
            self.lastSearchDepth += 1

            if value == item.value:
                return True
            else:
                if value < item.value:
                    item = item.left
                else:
                    item = item.right

        self.lastSearchDepth = originalLastSearchDepth
        return False

    def min(self):
        value = None
        item = self.parent
        originalLastSearchDepth = self.lastSearchDepth
        self.lastSearchDepth = 0

        while item is not None:
            self.lastSearchDepth += 1
            value = item.value
            item = item.left

        if value is None:
            self.lastSearchDepth = originalLastSearchDepth

        return value

    def max(self):
        value = None
        item = self.parent
        originalLastSearchDepth = self.lastSearchDepth
        self.lastSearchDepth = 0

        while item is not None:
            self.lastSearchDepth += 1
            value = item.value
            item = item.right

        if value is None:
            self.lastSearchDepth = originalLastSearchDepth

        return value

    def visitedNodes(self):
        return self.lastSearchDepth


def runTests():
    # bst.fromArray([-3835, 3508, 1222, -7011, -1991, 3026, -9913, 7103, -1298, 4016])
    print('\nBST 01:')
    bst1 = BinarySearchTree()

    print(bst1.search(10))
    print(bst1.visitedNodes())
    print(bst1.min())
    print(bst1.max())

    print('\nBST 02:')
    bst2 = BinarySearchTree()
    bst2.fromArray([5, 3, 1, 4, 7, 6, 8])

    print(bst2.search(5))
    print(bst2.visitedNodes())
    print(bst2.search(7))
    print(bst2.visitedNodes())
    print(bst2.search(6))
    print(bst2.visitedNodes())
    print(bst2.search(10))
    print(bst2.visitedNodes())
    print('MIN: ' + str(bst2.min()))
    print(bst2.visitedNodes())
    print('MAX: ' + str(bst2.max()))
    print(bst2.visitedNodes())

    print('\nBST 03:')
    bst3 = BinarySearchTree()
    bst3.fromArray([1, 3, 4, 5, 6, 7, 8])

    print('MIN: ' + str(bst3.min()))
    print(bst3.visitedNodes())
    print('MAX: ' + str(bst3.max()))
    print(bst3.visitedNodes())

runTests()
