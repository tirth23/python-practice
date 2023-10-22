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

    def insertAt(self, prev_value, new_value):
        temp = self.head

        while temp:
            if temp.data == prev_value:
                new_node = Node(new_value)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next

        print("No Node found")

    def append(self, new_value):
        new_node = Node(new_value)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def deleteNode(self, key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return   

        while temp is not None:
            if temp.data == key:
                break 
            prev = temp
            temp = temp.next
        prev.next = temp.next
        temp = None

        if temp == None:
            return

    def deletetotallist(self):
        curr = self.head                                #temp = self.head

        while curr:                                     #while temp:
            nxt = curr.next                                     #prev = temp
            self.head = nxt                                     #temp = temp.next
            del curr.data                                       #self.head = temp
            curr = nxt                                          #prev = None

    def getnodecount(self, node):
        if not node:
            return 0
        else:
            return 1 + self.getnodecount(node.next)

    def getcount(self):
        return self.getnodecount(self.head)

    def linkedreverse(self):
        prev = None
        current = self.head

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def printlist(self):
        tmp = self.head
        while tmp:
            print(tmp.data)
            tmp = tmp.next

    '''#convert singly linkedlist to circular linkedlist
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
                    break'''

if __name__ == "__main__":
    llist = LinkedList()

    llist.append(3)
    llist.push(4) 
    llist.insertAt(4, 2)
    llist.insertAt(3, 6)
    llist.insertAt(2, 0)
    llist.append(9)
    llist.deleteNode(4)
    llist.deleteNode(0)
    llist.deleteNode(9)
    #llist.deletetotallist()    
    print(llist.getnodecount(llist.head))
    print(llist.getcount())
    llist.linkedreverse()
    #llist.tocircular()
    llist.printlist()