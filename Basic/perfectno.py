'''perfect number is that number whose sum of factors excluding itself is number itself
    6 : 1, 2, 3, 6
    1 + 2 + 3 = 6(perfect number)
    
another definition: perfect number is that number whose sum of factors including itself and dividing it by 2 is number itself
    6 : 1, 2, 3, 6
    1 + 2 + 3 + 6 = 12
    12/2 = 6(perfect number)
    
    any given number is perfectly divisible by number less than or equal to half of given number
'''
def check(num):
    
    sum = 0
    for i in range(1, num//2 + 1):                         #number itself is not included
        
        if num % i == 0:
            sum += i

    if sum == num:
        print(num, "is perfect number.")
    else:
        print(num, "is not perfect number.")

if __name__ == "__main__":
    
    num = int(input("Enter number to check whether it is perfect or not : "))
    check(num)
    