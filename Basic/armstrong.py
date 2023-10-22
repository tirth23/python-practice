# 153 = 1^3+5^3+3^3, 1634 = 1^4+6^4+3^4+4^4, 0 to 9 = num^1
def armstrong(num):
    
    order = len(str(num))
    sum, temp = 0, num 
    
    while temp > 0:
        flag = temp % 10   
        sum = sum + flag ** order
        temp = temp // 10
    
    if num == sum:
        print(num, "is armstrong number.")
    else:
        print(num, "is not armstrong number.")
        
if __name__ == "__main__":
    
    n = int(input("Enter number to check armstrong or not : "))   
    armstrong(n)