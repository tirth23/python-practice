#pascal triangle gives coefficient of binomial expansion.
''' i
    1       1             0C0
    2      1 1         1C0   1C1
    3     1 2 1      2C0  2C1   2C2
'''
 
def fact(n):
    f = 1
    while n >= 1:
        f = f * n
        n-=1
    return f

def combination(n, r):

    return fact(n)//(fact(n-r) * fact(r))

def pascal(line):

    for i in range(1, line + 1):

        k,r = 1, 0
        for j in range(1, line * 2):

            if j >= line+1-i and j <= line-1+i and k:
                print(combination(i-1, r), end=" ")
                k = 0
                r+=1
            else:
                print(end="  ")
                k = 1
        
        print()

if __name__ == "__main__":
    
    pascal(5)
