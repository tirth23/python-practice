class Node:

    def __init__(self, new_value):
        self.data = new_value
        self.next = None

class CircularLinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_value):
        new_node = Node(new_value)
        temp = self.head
        new_node.next = self.head
        while temp:
            if temp.next == self.head:
                temp.next = new_node
                break
            temp = temp.next
        if temp == None:
            new_node.next = new_node
        self.head = new_node

    def insert(self, previous_value, new_value):
        new_node = Node(new_value)
        temp = self.head
        
        while temp:
            if temp.data == previous_value:
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
        print("No such previous value is found.")

    def append(self, new_value):
        new_node = Node(new_value)
        temp = self.head
        if temp == None:
            self.push(new_value)
        while temp:
            if temp.next == self.head:
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
        
    def delete(self, value):
        temp = self.head
        while temp:
            if temp.data == value and temp == self.head:
                if temp.next == self.head:
                    temp = None
                    self.head = None
                    return
                else:
                    while temp:
                        if temp.next == self.head:
                            temp.next = self.head.next
                            self.head = None
                            self.head = temp.next
                            return     
                        temp = temp.next
            elif temp.data == value:
                    prev_node.next = temp.next
                    temp = None
                    return
            else:
                if temp.next == self.head:
                    print("No such node found which can be deleted.")
                    return
            prev_node = temp
            temp = temp.next

    def deleteAll(self):
        temp = self.head
        while temp:
            if temp.next == self.head:
                temp.next = self.head.next
                self.head = self.head.next
                if self.head == temp:
                    self.head = None
                    temp = None
                    break
            temp = temp.next

        print("CircularLinkedList is deleted.")

    def count(self):
        temp = self.head
        count = 1
        while temp.next != self.head:
            count += 1
            temp = temp.next
        print(f"Node/s : {count}")

    def reverse(self):
        temp = self.head
        next_node = None
        while temp.next != self.head:
            temp = temp.next
        previous_node = temp

        while self.head != temp:
            next_node = self.head.next
            self.head.next = previous_node
            previous_node = self.head
            self.head = next_node
            if self.head == temp:
                self.head.next = previous_node

        print("CircularLinkedList is Reversed.")
           
    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break

    '''#convert circular linkedlist to linear linkedlist
    def toLinearLinkedList(self):
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = None

    def printLinearLinkedList(self):
        temp = self.head
        print("\nConverted to Linear LinkedList.")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next'''


if __name__ == "__main__":

    cllist = CircularLinkedList()
    cllist.append(9)
    cllist.push(7)
    cllist.push(6)
    cllist.push(5)
    cllist.insert(7, 8)
    cllist.append(10)
    cllist.delete(5)
    #cllist.deleteAll()
    cllist.count()
    cllist.reverse()
    cllist.push(11)
    cllist.print()
    #cllist.toLinearLinkedList()
    #cllist.printLinearLinkedList()