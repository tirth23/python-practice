#static
def find_gcd(x, y): 
	while(y): 
		x, y = y, x % y 

	return x 
	
	
l = [2, 4, 6, 8, 16] 

num1=l[0] 
num2=l[1] 
gcd=find_gcd(num1,num2) 

for i in range(2,len(l)): 
	gcd=find_gcd(gcd,l[i]) 
	
print(f"GCD is {gcd}") 

#dynamic
def find_gcd(x, y): 
	while(y): 
		x, y = y, x % y 

	return x 
	
	
if __name__ == "__main__":
    
    count = int(input("For how many numbers gcd is to be calculated : "))
    print("Enter numbers : ")
    
    l = []
    for i in range(0, count):
        
        num = int(input())
        l.append(num)
        
    num1 = l[0] 
    num2 = l[1] 
    gcd = find_gcd(num1, num2) 

    for i in range(2, len(l)): 
        
        gcd = find_gcd(gcd, l[i]) 
        
    print(f"GCD is {gcd}") 
    
#dynamic without list
def find_gcd(x, y): 
	while(y): 
		x, y = y, x % y 

	return x 
	
if __name__ == "__main__":
    
    count = int(input("For how many numbers gcd is to be calculated :  \b"))
    print("Enter numbers : ")
    
    gcd = 0
    for i in range(0, count):
        
        num = int(input())
        gcd = find_gcd(num, gcd)
        
    print(f"GCD is {gcd}") 