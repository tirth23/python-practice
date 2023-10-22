def fact(n):
    ans = 1
    for i in range(2, n+1):
        ans =  ans * i
    return ans

def combination(n ,r):
    return fact(n)/(fact(r)*fact(n-r))

n = 5
r = 3
print("Combination : ",int(combination(n, r)))