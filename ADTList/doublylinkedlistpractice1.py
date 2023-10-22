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

        if self.head != None:
            self.head.prev = new_node
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
    
    def append(self, new_value):
        new_node = Node(new_value)
        temp = self.head

        if self.head is None:
            self.push(new_value)

        while temp:
            if temp.next == None:
                new_node.next = temp.next
                temp.next = new_node
                new_node.prev = temp
                return
            temp = temp.next

    def delete(self, value):
        temp = self.head

        if temp == None:
            print("No node to be deleted.")

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

        gc.collect()      
                
    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

if __name__ == "__main__":

    dllist = DoublyLinkedList()
    dllist.append(10)
    dllist.insert(10, 2)
    dllist.push(8)
    dllist.push(5)
    dllist.insert(8, 0)
    dllist.delete(0)
    dllist.push(1)
    dllist.insert(1, 2)
    dllist.append(3)
    dllist.print()