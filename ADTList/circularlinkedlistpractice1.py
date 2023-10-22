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
        new_node.next = temp

        if temp != None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            self.head = new_node
            return
        else:
            new_node.next = new_node
            self.head = new_node
            return
    
    def delete(self, value):
        temp = self.head
        previous_node = None

        while temp:
            if temp.data == value and temp == self.head:
                if temp.next == temp:
                    temp = None
                    self.head = None
                    return
                else:
                    while temp.next != self.head:
                        temp = temp.next
                    temp.next = self.head.next
                    self.head = self.head.next
                    temp = None
                    return
            elif temp.data == value:
                previous_node.next = temp.next
                temp = None
                return
            else:
                if temp.next == self.head:
                    break
            previous_node = temp
            temp = temp.next

    def count(self):
        temp = self.head
        count = 1
        while temp.next != self.head:
            count += 1
            temp = temp.next
        print(count)

    def print(self):
        temp = self.head
        while True:
            print(temp.data)
            if temp.next == self.head:
                break
            temp = temp.next

if __name__ == "__main__":

    clist = CircularLinkedList()

    clist.push(10)
    clist.push(9)
    clist.push(8)
    #clist.delete(9)
    clist.delete(8)
    clist.count()
    clist.print()
    