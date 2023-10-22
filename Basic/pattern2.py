for i in range(1, 5):
    
    k = 65
    for j in range(1, 8):

        if j <= 5-i or j >= 3+i:
            print(chr(k), end="")
            if j < 4:
                k+=1
            else:
                k-=1
        else:
            print(end=" ")
            if j == 4:
                k-=1
        
    print()


for i in range(1, 8):

    for j in range(1, 8):
        
        if i<=4:
            if j >= 5-i and j <= 3+i:
                print("*", end=" ")
            else:
                print(end="  ")
        else:
            if j >= i-3 and j <= 11-i:
                print("*", end=" ")
            else:
                print(end="  ")
            
    print()

def star(rows):
    k = 0
    n = int((rows + 1)/2)
    for i in range(1, rows + 1):
        if rows%2 == 0:
            if i <= n: 
                k+=1
            if i >= n+2:
                k-=1
        else:
            if i <= n:
                k+=1
            else:
                k-=1
        for j in range(1, rows + 1):
            if j >= (n+1)-k and j <= (n-1)+k:
                print("*", end=" ")
            else:
                print(end="  ")
            
        print()

star(10)

k = 0
for i in range(1, 6):
    if i <= 3:
        k += 1
    else:
        k -= 1
    for j in range(1, 6):
        if j >= 4-k and j <= 2+k:
            print("*", end=" ")
        else:
            print(end="  ")
    print()