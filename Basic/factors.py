def factors(num):
    
    print(f"Factors of {num} : ", end="")
    for i in range(1, num + 1):
        
        if num % i == 0:
            print(i, end=" ")
    
if __name__ == "__main__":
    
    num = int(input("Enter number to find factors : "))
    factors(num)