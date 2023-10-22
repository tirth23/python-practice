x = 1.4
a = int(1.4)
print(x, a)
b = "0" + "b"
print(b)

class a:
    def f(self):
        print("hi")

a = a()
a.f()
print(type(a))

# For list of integers 
#lst1 = [] 

# For list of strings/chars 
#lst2 = [] 

lst1 = input("Enter the list items : ").split()

lst2 = [int(item) for item in input("Enter the list items : ").split()] 


lst3 = [print(int(item)) for item in input("Enter the list items : ").split()] 
print(input())
print(lst1) 
print(lst2) 
print(lst3) 

x, y = input().split() 
print(x, y)

x, y = input().split()
print(x, y)
x, y = [5, 6]
print(x, y)
x, y = input(), input()
print(x, y)

x, y = [int(x), int(y)]
x, y = [int(x) for x in [x, y]]
print(x, y)

print(list(range(5)))

txt = """apple#banana#cherry#
orange"""

x = txt.split("\n")

print(x)