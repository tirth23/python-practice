#circularqueue implementation using array
class CircularQueue: 
 
	def __init__(self, capacity): 
		self.front = self.size = 0
		self.rear = capacity -1
		self.queue = [None]*capacity 
		self.capacity = capacity 
	
	def isFull(self): 
		return self.size == self.capacity 
	
	def isEmpty(self): 
		return self.size == 0

	def EnQueue(self, item): 
		if self.isFull(): 
			print("Full") 
			return
		self.rear = (self.rear + 1) % (self.capacity) 
		self.queue[self.rear] = item 
		self.size = self.size + 1
		print("% s enqueued to queue" % str(item)) 

	def DeQueue(self): 
		if self.isEmpty(): 
			print("Empty") 
			return
		
		print("% s dequeued from queue" % str(self.queue[self.front])) 
		self.front = (self.front + 1) % (self.capacity) 
		self.size = self.size -1
		
	def que_front(self): 
		if self.isEmpty(): 
			print("Queue is empty")
		print("Front item is", self.queue[self.front]) 
		
	def que_rear(self): 
		if self.isEmpty(): 
			print("Queue is empty") 
		print("Rear item is", self.queue[self.rear])

	def print(self):
		count = (self.rear+self.capacity-self.front) % self.capacity + 1
		print("Queue : ")
		for i in range(count):
			index = (self.front+i) % self.capacity
			print(self.queue[index], end= " ")
		print()

if __name__ == '__main__':
	
	cq = CircularQueue(3)
	cq.EnQueue(10)
	cq.EnQueue(20)
	cq.EnQueue(30)
	cq.DeQueue()
	cq.EnQueue(1)
	cq.que_front()
	cq.que_rear()
	cq.print()