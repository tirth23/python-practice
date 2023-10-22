def pat(rows):
    for i in range(1, rows + 1):
        
        for j in range(rows, i - 1, -1):

            if j % 2 != 0:
                print(j, end=" ")
            print("*", end=" ")
        print()

pat(5)

def pat(rows):
    for i in range(1, rows + 1):
        
        for j in range(rows, i - 1, -1):

            if j % 2 != 0:
                print(j, end=" ")
            else:
                for i in range(1, j + 1):
                    print("*", end=" ")
        print()

pat(5)

def ro(rows):

    for i in range(1, rows + 1):

        for j in range(1, i):
            print(" ", end="")     #print(" ", end=" ") it will print below example

        if i == 1 or i == rows:
            for j in range(1, rows + 1):
                print("* ", end="")
        else:
            for i in range(1, rows + 1):
                if i == 1 or i == rows:
                    print("* ", end="")
                else:
                    print("  ", end="")
        print()

ro(5)

for i in range(1, 6):

    for j in range(1, 10):
        
        if i == 1 or i == 5:
            if j >= i and j <= i+4:
                print("* ", end="")
            else:
                print(end="  ")
        else:
            if j == i or j == i+4:
                print("* ", end="")
            else:
                print(end="  ")
    print()

def pat1():
    for i in range(1, 6):
        for j in range(1, 6):
            if j <= 6-i:
                if j % 2 != 0:
                    print(6-j, end=" ")
                else:
                    for k in range(1, 6-j+1):
                        print("*", end=" ")
        print()

pat1()