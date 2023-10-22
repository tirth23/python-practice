#Array implementation
class Stck:

    def __init__(self, size):
        self.top = -1
        self.size = size
        self.st = [None for i in range(size)]

    def isfull(self):
        if self.top == self.size-1:
            print("Stack is full.")
            return 1
    
    def isempty(self):
        if self.top == -1:
            print("Stack is empty.")
            return 1

    def push(self, new_value):
        if self.isfull():
            return
        self.top += 1
        self.st[self.top] = new_value

    def pop(self):
        if self.isempty():
            return
        top = self.st[self.top]
        print(f"{top} is popped.")
        self.top -= 1

    def printstack(self):
        if self.isempty():
            return
        # o to top+1 in reverse
        for i in range(self.top, -1, -1):
            print(self.st[i], end=" ")
        print()

    def switch(self, arg):
        if arg == 1:
            new_value = int(input("Enter value to push : "))
            sta.push(new_value)
        elif arg == 2:
            sta.pop()
        elif arg == 3:
            sta.printstack()
        else:
            print("Enter value between 1 and 3.")

if __name__ == "__main__":
    
    size = int(input("Enter the size of stack : "))
    sta = Stck(size)
    flag = '1'
    while flag == '1':
        print("Main Menu\n 1. Push\n 2. Pop\n 3. Print")
        arg = int(input("Enter your choice : "))
        sta.switch(arg)
        flag = input("Press 1 to continue or press any key to exit : ")
        
    
