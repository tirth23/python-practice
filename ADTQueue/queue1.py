'''#worst approach for queue
mylist = []
mylist.append("superman")
mylist.append("batman")
mylist.append("flash")
print(mylist)
mylist.pop(0)
print(mylist)'''

from collections import deque
mylist = deque()
mylist.append("superman")
mylist.append("batman")
mylist.append("flash")
print(mylist)
#popleft is better than pop(0) as in pop(0) all elements need to be assigned everytime after deletion
mylist.popleft()
mylist.popleft()
mylist.popleft()
#mylist.popleft()
print(mylist)

