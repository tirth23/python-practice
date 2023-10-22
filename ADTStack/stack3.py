#LinkedList implementation
class Node:
    def __init__(self, new_value):
        self.data = new_value
        self.next = None

class stck:
    def __init__(self):
        self.head = None

    def push(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head != None:
            data = self.head.data
            print(f"{data} is popped.")
            self.head = self.head.next
            return
        print("Stack is empty.")

    def print(self):
        temp = self.head
        if temp != None:
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            return
        print("Stack is empty.")

if __name__ == '__main__':

    sta = stck()
    sta.push(3)
    sta.push(2)
    sta.push(1)
    sta.pop()
    sta.print()
