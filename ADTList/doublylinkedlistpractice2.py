import gc

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkList:
    def __init__(self):
        self.head = None

    def push(self, new_value):
        new_node = Node(new_value)

        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def addatlast(self, new_value):
        new_node = Node(new_value)
        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        last = self.head
        while(last.next is not None):
            last = last.next

        last.next = new_node
        new_node.prev = last
        return

    def deletenode(self, key):

        if self.head is None or key is None:
            return print("key seems to be none! Please pass some value")

        #case 1
        if self.head == key:
            self.head = key.next

        #case 2
        if key.next is not None:
            key.next.prev = key.prev

        #case 3
        if key.prev is not None:
            key.prev.next = key.next

        gc.collect()

    def deleteNode(self, key):
        temp = self.head

        if self.head is None or key is None:
            return print("either head is empty or key is none")

        # case 1: if head is the key or key at very first position
        if temp.data == key:
            self.head = temp.next
            temp = None
            return

        while temp is not None:
            #case 2:
            if temp.data == key and temp.next is not None:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                return

            # case 3:
            if temp.data == key and temp.next is None:
                temp.prev.next = None
                return

            #case 4:
            if temp.data == key and temp.prev is not None:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                return

            temp = temp.next

        gc.collect()

    def printdlist(self, node):
        while(node is not None):
            print(node.data, end=" ")
            node = node.next


dllist = DoublyLinkList()
dllist.push(1)
dllist.push(2)
dllist.push(3)
dllist.addatlast(4)
dllist.addatlast(5)
dllist.printdlist(dllist.head)
print()
dllist.deleteNode(4)
dllist.printdlist(dllist.head)
