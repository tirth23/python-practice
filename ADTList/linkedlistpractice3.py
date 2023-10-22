class Node:
    def __init__(self, new_value):
        self.data = new_value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node
        return
    
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
        temp = self.head

        if temp is None:
            self.push(new_value)
            return
        
        while temp:
            if temp.next is None:
                new_node = Node(new_value)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next

    def printl(self):
        temp = self.head

        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        
if __name__ == "__main__":
    llist = Linkedlist()

    llist.append(3)
    llist.push(4) 
    llist.insertAt(4, 2)
    llist.insertAt(3, 6)
    llist.insertAt(2, 0)
    llist.append(9)
    llist.push(4) 
    llist.printl()    