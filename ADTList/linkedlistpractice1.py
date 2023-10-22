class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

    def insertAt(self, prev_node, new_value):
        temp = self.head
        temp2 = None
        while temp:
            if temp.data == prev_node:
                temp2 = temp
                break
            temp = temp.next
        prev_node = temp2
        if prev_node is None:                                    
            print("Previous node seems to be empty")
        else:
            new_node = Node(new_value)
            new_node.next = prev_node.next
            prev_node.next = new_node

    def append(self, new_value):
        new_node = Node(new_value)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def printlist(self):
        tmp = self.head
        while tmp:
            print(tmp.data)       
            tmp = tmp.next

    '''    #convert singly linkedlist to circular linkedlist
    def tocircular(self):
        start = self.head

        while self.head.next is not None:
            self.head = self.head.next

        self.head.next = start
        print("Done")
        return start

    def printlist(self):
        temp = self.head

        if self.head is not None:
            while True:
                print(temp.data)
                temp = temp.next
                if temp == self.head:
                    break
    '''

if __name__ == "__main__":
    llist = LinkedList()

    llist.append(3)
    llist.push(4)
    llist.insertAt(3, 2)
    llist.insertAt(2, 6)
    llist.append(10)
    llist.insertAt(10, 6)
    #llist.tocircular()
    llist.printlist()    