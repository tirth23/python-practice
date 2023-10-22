class Node:

    def __init__(self, value):
        self.data = value
        self.next =None


n = Node(1)
m = Node(2)
n = m
print(n.data)
print(n)
print(m)


a,b = 400, 400.0
if  a==b:
    print("yes")

print(3-4.587)

num = str(input())
print(int(num,10))

for i in range(65, 65+25):
    print(chr(i), end = " , ")

