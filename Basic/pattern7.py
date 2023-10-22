def pat(n):
    for i in range(1, 3*n+1):

        for j in range(1, (2*n-1)+1):

            if i <= n:
                if j >= 2*n-i:
                    print("*", end=" ")
                else:
                    print(end="  ")

            elif i <= 2*n:
                if j==n:
                    print("|", end=" ")
                elif j <= i-(n+1):
                    print("*", end=" ")
                elif j >= i:
                    print("*", end=" ")
                else:
                    print(end="  ")
            
            elif i <= 3*n:
                if j <= (3*n+1)-i:
                    print("*", end=" ")
                else:
                    print(end="  ")
    
        print()

pat(3)


def fun(n):

    for i in range(1, n + 1):
        k = 1
        num = 1
        alpha = 65
        for j in range(1, (2*n-1)+1):
            if j >= n+1-i and j <= n-1+i:
                if k:
                    if i%2 == 1:
                        print(num, end="")
                        num+=1
                    else:
                        print(chr(alpha), end="")
                        alpha+=1
                else:
                    print(end=" ")
                k = 1 - k
            else:
                print(end=" ")
        
        print()

fun(6)

def method(num):
    a = 65
    for i in range(1, 5):
        p = a
        for j in range(1, 8):
            if j <= 5-i or j >= 3+i:
                print(chr(p), end=" ")
            else:
                print(end="  ")
            p+=1
        print()

print("-------------")
method(4)