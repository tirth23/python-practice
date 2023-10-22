#circularqueue implementation using array
class CircularQueue:

    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1
    
    def isfull(self):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full.")
            return 1

    def isempty(self):
        if self.front == -1 and self.rear == -1:
            return 1

    def enqueue(self, data):
        if self.isfull():
            return
        elif self.isempty():
            self.front = self.rear = 0 
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if self.isempty():
            print("Queue is already empty.")
            return
        elif self.front == self.rear:
            front = self.queue[self.front]
            print(f"{front} is dequeued.")
            self.front = self.rear = -1
        else:
            front = self.queue[self.front]
            print(f"{front} is dequeued.")
            self.front = (self.front + 1) % self.size

    def print(self):
        if self.isempty():
            print("Queue is already empty.")
            return
        i = self.front
        while(i != -1):
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i+1)%self.size
        print()


if __name__ == '__main__':

    cq = CircularQueue(4)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.dequeue()
    cq.enqueue(6)
    cq.enqueue(5)
    cq.dequeue()
    cq.enqueue(10)
    cq.print()

