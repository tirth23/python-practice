class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        temp = self.head

        new_node.next = self.head

        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node
    
    def delete(self, deleteval):
        current_node = self.head
        prev_node = None

        while current_node:

            if current_node.data == deleteval and current_node == self.head:
                #head is the only element
                if current_node.next == self.head:
                    current_node = None
                    self.head = None
                    return
                #there are more elements in list
                else:
                    #delete head and update head
                    while current_node.next != self.head:
                        current_node = current_node.next
                    current_node.next = self.head.next
                    self.head = self.head.next
                    #current_node = None
                    return
            elif current_node.data == deleteval:
                prev_node.next = current_node.next
                current_node = None
                return
            else:
                if current_node.next == self.head:
                    break

            prev_node = current_node
            current_node = current_node.next

    def count(self):
        current = self.head
        self.count = 1
        while current.next != self.head:
            self.count = self.count + 1
            current = current.next
        print(self.count)

    def print(self):
        temp = self.head
        
        if self.head is not None:
            while True:
                print(temp.data)
                temp = temp.next
                if temp == self.head:
                    break

if __name__ == "__main__":
    
    cllist = CircularLinkedList()
    cllist.push(10)
    cllist.push(9)
    cllist.push(8)
    cllist.delete(8)
    cllist.count()
    cllist.print()