def find_lcm(x, y):
    
    a, b = x, y
    while(y): 
	    x, y = y, x % y

    lcm = (a * b) / x
    return lcm
	
if __name__ == "__main__":
    
    count = int(input("For how many numbers lcm is to be calculated :  \b"))
    print("Enter numbers : ")
    
    lcm = 1
    for i in range(0, count):
        
        num = int(input())
        lcm = find_lcm(num, lcm)
        
    print(f"LCM is {lcm}") 