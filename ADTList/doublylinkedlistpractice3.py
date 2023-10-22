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
        temp = self.head
        new_node.next = self.head
        if temp != None:
            temp.prev = new_node
        self.head = new_node

    def insert(self, previous_value, new_value):
        new_node = Node(new_value)
        temp = self.head
        while temp:
            if temp.data == previous_value:
                new_node.next = temp.next
                temp.next = new_node
                new_node.prev = temp
                if new_node.next != None:
                    new_node.next.prev = new_node
                return
            temp = temp.next
        print("No such node found.")

    def append(self, new_value):
        new_node = Node(new_value)
        temp = self.head
        if temp == None:
            self.head = new_node

        while temp:
            if temp.next == None:
                temp.next = new_node
                new_node.prev = temp
                return
            temp = temp.next 

    def delete(self, value):
        temp = self.head
        if temp.data == value and temp == self.head:
            self.head = temp.next
            temp = None
            return

        while temp:
            if temp.data == value:
                temp.prev.next = temp.next
                if temp.next != None:
                    temp.next.prev = temp.prev
                temp = None
                return
            temp = temp.next

        print("No such node found which can be deleted.")

    def deleteAll(self):
        temp = self.head
        while temp:
           prev = temp
           self.head = temp.next
           perv = None
           temp = temp.next
           temp.prev = None
        print("Doubly LinkedList is deleted.")

    def count(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        print(f"Node/s : {count}")

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end = " ")
            temp = temp.next

    '''def toCircularDoublyLinkedList(self):
        temp = self.head
        while temp:
            if temp.next == None:
                temp.next = self.head
                self.head.prev = temp
                break
            temp = temp.next
        print("\nConverted to Circular Doubly LinkedList.")

    def printCircularDoublyLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data, end = " ")
            if temp.next == self.head:
                break
            temp = temp.next'''

if __name__ == "__main__":
    
    dllist = DoublyLinkedList()
    dllist.append(13)
    dllist.push(10)
    dllist.push(9)
    dllist.insert(10, 12)
    dllist.insert(10, 11)
    dllist.append(14)
    dllist.delete(14)
    #dllist.deleteAll()
    dllist.count()
    dllist.delete(9)
    dllist.print()
    #dllist.toCircularDoublyLinkedList()
    #dllist.printCircularDoublyLinkedList()
   