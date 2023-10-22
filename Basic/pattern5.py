k = 1
for i in range(1, 6):
    p = k
    for j in range(1, 10):

        if j <= 2*i-1:
            if i % 2 != 0:
                if j % 2 == 0:
                    print("*", end="")
                else:
                    print(p, end="")
                    p+=1
            else:
                if j % 2 == 0:
                    print("*", end="")
                else:
                    print(p, end="")
                    p-=1

        else:
            print(end=" ")
    k+=1
        
    print()


k = 64
for i in range(1, 6):
    k = k + i
    a = k
    for j in range(1, 6):

        if j >= 6-i:
            print(chr(a),end=" ")
            a-=1
        else:
            print(end="  ")

    print()

def ms(rows):
    k = 1
    for i in range(1, rows + 1):
        p = k
        
        for j in range(1, i+1):
            print(p, end=" ")
            p = p - ((rows-i)+j)

        k = k + ((rows + 1) - i)
        print()

ms(5)

k = 0
flag = 1
for i in range(1, 8):
    
    if i < 4-k:
        print(end=" ")
    else:
        if flag:
            print("*", end="")
        else:
            print(end=" ")
        flag = 1 - flag

    if i == 4+k:
        k+=1
        print()
        if i==7:
            break
        i = 0
        flag = 1
  

