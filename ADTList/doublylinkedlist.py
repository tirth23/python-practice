import gc

class Node:
    def __init__(self, new_value):
        self.data = new_value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node
        
        self.head = new_node

    def insert(self, prev_node, new_value):

        if prev_node is None:
            print("prev_node can not be None.")

        new_node = Node(new_value)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        if new_node.next is not None:
            new_node.next.prev = new_node
        
    def append(self, new_value):
        new_node = Node(new_value)
        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = last
        return

    def delete(self, key):
        if self.head is None or key is None:
            return

        if self.head == key:
            self.head = key.next

        if key.next is not None:
            key.next.prev = key.prev

        if key.prev is not None:
            key.prev.next = key.next

        gc.collect()

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":
    dllist = DoublyLinkedList()

    dllist.push(10)
    dllist.push(9)
    dllist.push(8)
    dllist.insert(dllist.head.next, 7)
    dllist.append(11)
    dllist.delete(dllist.head.next)
    dllist.print()