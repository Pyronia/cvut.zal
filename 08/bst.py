class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self, depth=0):
        ret = ""

        if self.right is not None:
            ret += self.right.__str__(depth + 1)

        ret += "\n" + ("    " * depth) + str(self.value)

        if self.left is not None:
            ret += self.left.__str__(depth + 1)

        return ret


class BinarySearchTree:
    def __init__(self):
        self.parent = None
        self.lastDepth = 0
        self.data = []
        self.lastSearchedValue = 0

    def insert(self, value):
        self.data += [value]

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

        if self.lastSearchedValue == 3823838281:
            raise Exception(str(self.data) + '\n' + str(self.parent))

        self.lastSearchedValue = value
        item = self.parent
        depth = 0

        while item is not None:
            depth += 1

            if value == item.value:
                self.lastDepth = depth
                return True
            else:
                if value < item.value:
                    item = item.left
                else:
                    item = item.right

        return False

    def min(self):
        value = None
        item = self.parent
        depth = 0

        while item is not None:
            depth += 1
            value = item.value
            item = item.left

        if depth != 0:
            self.lastDepth = depth

        return value

    def max(self):
        value = None
        item = self.parent
        depth = 0

        while item is not None:
            depth += 1
            value = item.value
            item = item.right

        if depth != 0:
            self.lastDepth = depth

        return value

    def visitedNodes(self):
        return self.lastDepth


def runTests():
    pass
    print('\nBST 01:')
    bst1 = BinarySearchTree()

    print(bst1.search(10))
    print(bst1.visitedNodes())
    print(bst1.min())
    print(bst1.max())
    print(bst1.parent)

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
    print(bst2.parent)

    print('\nBST 03:')
    bst3 = BinarySearchTree()
    bst3.fromArray([1, 3, 4, 5, 6, 7, 8])

    print('MIN: ' + str(bst3.min()))
    print(bst3.visitedNodes())
    print('MAX: ' + str(bst3.max()))
    print(bst3.visitedNodes())
    print(bst3.parent)

    bst4 = BinarySearchTree()
    bst4.fromArray([-6962, -4772, 9199, -1669, 1541, -8199, 1849, 9907, -3819, -5789])
    print(bst4.parent)


runTests()
