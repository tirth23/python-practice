class Node:

    def __init__(self, data):
        self.data = data
        self.height = 0
        self.leftChild = None
        self.rightChild = None

class AVL:

    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insertNode(data, self.root)

    def insertNode(self, data, node):

        if not node:
            return Node(data)

        if data < node.data:
            node.leftChild = self.insertNode(data, node.leftChild)
        else:
            node.rightChild = self.insertNode(data, node.rightChild)

        return node

    def traverse(self):
        if self.root:
            self.traverseInorder(self.root)

    def traverseInorder(self, node):

        if node.leftChild:
            self.traverseInorder(node.leftChild)
        print(node.data)
        if node.rightChild:
            self.traverseInorder(node.rightChild)

if __name__ == "__main__":

    avl = AVL()
    avl.insert(1)
    avl.insert(0)
    avl.insert(0)
    avl.insert(6)
    avl.insert(15)
    avl.traverse()