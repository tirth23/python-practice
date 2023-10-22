number = int(input("Enter number : "))
n1,n2,count = 0, 1, 1
while count <= number:
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    count += 1

# Another method with recursion
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) +  fib(n-2)

count = number
if count <= 0:
    print("Enter number greater than 2")
else:
    for i in range(count):
        print(fib(i), end=" ")