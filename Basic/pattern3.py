def p(rows):
    k = 0
    for i in range(1, rows + 1):
        if rows%2 == 0:
            if i <= rows/2:
                k+=1
            if i >= (rows/2) + 2:
                k-=1
        else:
            if i <= 4:
                k+=1
            else:
                k-=1
        for j in range(1, rows + 1):
            if j <= k:
                print("* ", end="")
            else:
                print(end="  ")
        print()

p(7)
p(8)

for i in range(1, 6):
    k = 0
    for j in range(1, 6):

        if j <= i:
            print(k, end=" ")
            k = k + i - 1
        else:
            print(end="  ")

    print()

for i in range(1, 6):
    k = 0
    for j in range(1, 6):
        if j <= i:
            print(k*(i-1), end=" ")
            k += 1
        else:
            print(end="  ")
    print()