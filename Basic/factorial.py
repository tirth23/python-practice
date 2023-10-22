def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1)

num = 7
if num < 0:
    print("No negative numbers")
elif num == 0:
    print("Factorial is 1")
else:
    print("Factorial is ", fact(num))

#Another method
num, ans= 7, 1
while num != 1:
    ans *= num
    num -=1
print(ans)
