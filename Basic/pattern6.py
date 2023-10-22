def z(rows):
    for i in range(1, rows + 1):

        if i == 1 or i == rows:
            for j in range(1, rows + 1):
                print("*", end=" ")
        else:
            for j in range (rows - 2, i-2, -1):
                print(" ", end=" ")
            #for i in range(1,2):
            print("*", end=" ")
        print()

z(5)

import math
def t(rows):
    for i in range(1, rows+1):

        for j in range(1, rows+1):
            if i == 1:
                print("*", end=" ")
            else:
                if j == (int(rows/2)+1) or j == rows/2 :
                    print("*", end=" ")
                else:
                    print(end="  ")
        print()

t(7)
t(8)

def a(rows):
    for i in range(1, rows + 1):

        for j in range(1, (rows*2-1)+1):

            if i == int(rows/2)+1:
                if j >= 3 and j <= 7:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            else:
                if j == 6-i or j == 4+i:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            
        print()

a(5)