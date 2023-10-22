'''strong number is that number whose factorial of digits is same as number
145 = 1! + 4! + 5!
'''
def fact(n):
    
    s = 1
    while n >= 1:
        s = s * n
        n -= 1
    return s
    
def strong(num):
    
    sum = 0
    temp = num
    while temp > 0:
        flag = temp % 10
        sum = sum + fact(flag)
        temp = temp // 10
         
    if sum == num:
        print(f"{num} is strong number.")
    else:
        print(f"{num} is not strong number.")
        
if __name__ == "__main__":
    
    num = int(input("Enter number to check whether number is strong or not : "))
    strong(num) 