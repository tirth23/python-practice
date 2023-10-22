#queue implementation using linkedlist
class Node:
    def __init__(self, new_value):
        self.data = new_value
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isempty(self):
        if self.front == None and self.rear == None:
            return 1

    def enqueue(self, new_value):
        new_node = Node(new_value)
        if self.isempty():
            self.rear = new_node
            self.front = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        temp = self.front
        if self.isempty():
            print("Queue is empty.")
            return
        elif temp.next == None:
            front = temp.data
            print(f"{front} is dequeued.")
            self.front = self.rear = None
        else:
            front = temp.data
            print(f"{front} is dequeued.")
            self.front = temp.next

    def print(self):
        if self.isempty():
            print("Queue is empty.")
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

if __name__ == "__main__":
    
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.dequeue()
    q.print()