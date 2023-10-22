from queue import Queue
mylist = Queue()
mylist.put("superman")
mylist.put("aquaman")
mylist.put("flash")
print(mylist)
print(mylist.get())                           #get is dequeue
print(mylist.get())
#print(mylist.get())
print(mylist)
#print(mylist.get())
mylist.get_nowait()     #to check whether list is empty or not