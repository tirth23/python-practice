#queue implementation using array
class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def isfull(self):
        if self.rear == self.size-1 and self.front != self.size:
            print("Queue is full.")
            return 1
    
    def isempty(self):
        if self.front == -1 and self.rear == -1 or self.front > self.rear:
            print("Queue is empty.")
            return 1

    def enqueue(self, new_value):
        if self.isfull():
            return
        elif self.front >= self.size :
            print("Capacity overloaded.")
            return
        elif self.front == -1 and self.rear == -1:
            self.front += 1
            self.rear += 1
            self.queue[self.rear] = new_value
        else:
            self.rear += 1
            self.queue[self.rear] = new_value
    
    def dequeue(self):
        if self.isempty():
            return
        else:
            front = self.queue[self.front]
            print(f"{front} is dequeued.")
            self.front += 1

    def print(self):
        if self.isempty():
            return
        for i in range(self.front, self.rear+1):
            print(self.queue[i], end=" ")
        print()

if __name__ == "__main__":
    
    size = int(input("Enter size of queue : "))
    q = Queue(size)
    q.enqueue(5)
    q.enqueue(4)
    q.dequeue()
    q.dequeue()
    q.enqueue(2)
    q.dequeue()
    q.enqueue(1)
    q.print()