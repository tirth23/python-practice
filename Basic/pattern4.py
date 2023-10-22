rows = 6
for num in range(rows):
    for i in range(num):
        print(num, end=" ")  # print number
    # line after each row to display pattern correctly
    print(" ")

for i in range(1,6):
    for j in range(1,i+1):
        print("*", end=" ")
    print('   ')

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(i, end=" ")
    print() 