class Node:

    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.height = 0

class AVL:

    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insertNode(data, self.root)

    def insertNode(self, data, curr_node):
        
        if curr_node is None:
            return Node(data)
        if data < curr_node.data:
            curr_node.leftchild = self.insertNode(data, curr_node.leftchild)
        else:
            curr_node.rightchild = self.insertNode(data, curr_node.rightchild)

        curr_node.height = max(self.getheight(curr_node.leftchild), self.getheight(curr_node.rightchild)) + 1
        balance = self.getbalance(curr_node)
        if balance > 1 or balance < -1:
            return self.settleViolation(data, curr_node, balance)
        else:
            return curr_node

    def settleViolation(self, data, curr_node, balance):

        if balance > 1:
            if data < curr_node.leftchild.data:
                return self.rotateRight(curr_node)
            else:
                curr_node.leftchild = self.rotateLeft(curr_node.leftchild)
                return self.rotateRight(curr_node)

        if balance < -1:
            if data > curr_node.rightchild.data:
                return self.rotateLeft(curr_node)
            else:
                curr_node.rightchild = self.rotateRight(curr_node.rightchild)
                return self.rotateLeft(curr_node)

    def rotateRight(self, curr_node):

        templeftchild = curr_node.leftchild
        temp = templeftchild.rightchild
        templeftchild.rightchild = curr_node
        curr_node.leftchild = temp

        templeftchild.height = max(self.getheight(templeftchild.leftchild), self.getheight(templeftchild.rightchild)) + 1
        curr_node.height = max(self.getheight(curr_node.leftchild), self.getheight(curr_node.rightchild)) + 1

        return templeftchild

    def rotateLeft(self, curr_node):

        temprightchild = curr_node.rightchild
        temp = temprightchild.leftchild
        temprightchild.leftchild = curr_node
        curr_node.rightchild = temp

        temprightchild.height = max(self.getheight(temprightchild.leftchild), self.getheight(temprightchild.rightchild)) + 1
        curr_node.height = max(self.getheight(curr_node.leftchild), self.getheight(curr_node.rightchild)) + 1

        return temprightchild

    def delete(self, data):
        if self.root:
            self.root = self.deleteNode(data, self.root)

    def deleteNode(self, data, curr_node):

        if curr_node is None:
            return curr_node
        if data < curr_node.data:
            curr_node.leftchild = self.deleteNode(data, curr_node.leftchild)
        elif data > curr_node.data:
            curr_node.rightchild = self.deleteNode(data, curr_node.rightchild)
        else:
            if curr_node.leftchild is None:
                temprightchild = curr_node.rightchild
                curr_node = None
                return temprightchild
            elif curr_node.rightchild is None:
                templefthild = curr_node.leftchild
                curr_node = None
                return templefthild
            tempNode = self.inorderSuccessor(curr_node.rightchild)
            curr_node.data = tempNode.data
            curr_node.rightchild = self.deleteNode(data, curr_node.rightchild)

        if curr_node is None:
            return curr_node

        curr_node.height = max(self.getheight(curr_node.leftchild), self.getheight(curr_node.rightchild)) + 1
        balance = self.getbalance(curr_node)

        if balance > 1:
            if self.getbalance(curr_node.leftchild) >= 0:
                return self.rotateRight(curr_node)
            else:
                curr_node.leftchild = self.rotateLeft(curr_node.leftchild)
                return self.rotateRight(curr_node)

        if balance < -1:
            if self.getbalance(curr_node.rightchild) <= 0:
                return self.rotateLeft(curr_node)
            else:
                curr_node.rightchild = self.rotateRight(curr_node.rightchild)
                return self.rotateLeft(curr_node)

        return curr_node

    def getheight(self, curr_node):
        if curr_node is None:
            return -1

        return curr_node.height

    def getbalance(self, curr_node):
        if curr_node is None:
            return 0

        return self.getheight(curr_node.leftchild) - self.getheight(curr_node.rightchild)

    def inorderSuccessor(curr_node):

        if curr_node:
            return self.inorderSuccessor(curr_node.leftchild)

        return curr_node

    def print(self):
        if self.root:
            self.inorder(self.root)

    def inorder(self, curr_node):
        if curr_node:
            self.inorder(curr_node.leftchild)
            print(curr_node.data)
            self.inorder(curr_node.rightchild)

if __name__ == "__main__":

    avl = AVL()
    avl.insert(14)
    avl.insert(17)
    avl.insert(11)
    avl.insert(7)
    avl.insert(53)
    avl.insert(4)
    avl.insert(13)
    avl.insert(12)
    avl.insert(8)
    avl.insert(60)
    avl.insert(19)
    avl.insert(16)
    avl.insert(20)
    avl.delete(20)
    avl.delete(17)
    avl.print()  