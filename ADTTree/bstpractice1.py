class Node:
    def __init__(self, new_value):
        self.left = self.right = None
        self.data = new_value

class BinarySearchTree:
    def __init__(self, root = None):
        self.root = root
    
    def get_root(self):
        return self.root

    def insert(self, new_value):
        new_node = Node(new_value)
        if self.root is None:
            self.root = new_node
        else:
            self.insert_helper(self.root, new_value)

    def insert_helper(self, current_node, new_value):
        new_node = Node(new_value)

        if new_node.data < current_node.data:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self.insert_helper(current_node.left, new_value)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self.insert_helper(current_node.right, new_value)

    def inordersuccessor(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def delete(self, current_node, value):
        
        if current_node is None:
            return current_node
        
        #finding key
        elif value < current_node.data:
            current_node.left = self.delete(current_node.left, value)
        elif value > current_node.data:
            current_node.right = self.delete(current_node.right, value)
        
        #key is matched with current_node so deletion starts
        else:
            #0 or 1 child
            if current_node.left is None:
                temp = current_node.right
                current_node = None
                return temp
            elif current_node.right is None:
                temp = current_node.left
                current_node = None
                return temp

            #2 children
            temp = self.inordersuccessor(current_node.right)
            current_node.data = temp.data
            current_node.right = self.delete(current_node.right, temp.data)   #delete inorder successor
            
        return current_node

    def search(self, current_node, value):
        if current_node is None:
            print("Value does not exist.")
            return False
        elif current_node.data == value:
            print("Value found.")
        elif value < current_node.data:
            self.search(current_node.left, value)
        else:
            self.search(current_node.right, value)

    def inorder(self, current_node):
        if current_node:
            self.inorder(current_node.left)
            print(current_node.data, end = " ")
            self.inorder(current_node.right)

    def print(self):
        print("Tree : ")
        self.inorder(self.root)
     
if __name__ == "__main__":
    
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(12)
    bst.insert(5)
    bst.insert(5)
    bst.insert(4)
    bst.insert(7)
    bst.insert(9)
    bst.insert(8)
    bst.insert(6)
    bst.insert(16)
    bst.delete(bst.root, 7)
    bst.search(bst.root, 0)
    bst.print()

