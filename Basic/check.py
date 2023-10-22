x=9
class example:
    c=1
    def ex(self):
        self.a=5
        self.b=4

    def eq(qw):
        global x
        x=50
        print(x)
        

q=example()
q.ex()
q.eq()
print(q.a)
print(q.c)

y=0
def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

        def inner1():
            x=1
            print("inner1:", x)

        inner1()
        print("inner:", x)

    inner()
    print("outer:", x)
    global y
    y=1
    print(y)


outer()

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname, self.lastname)
        
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
        
    def printname(self1):
        print("a")

x = Person("Mike", "Olsen")
x.printname()

l=[3,5,6]
it=iter(l)
for i in it:
    print(i)


print("h")
for x in l:
    print(x)

print(dir(list))

order = 4
for i in range(-4, 0, -1):
    print(i)
