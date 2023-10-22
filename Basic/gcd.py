# gcd(0, a) = a gcd(1, a) = 1
def gcd(a,b): 
	
	if (a == 0): 
		return b 
	if (b == 0): 
		return a 
 
	if (a == b): 
		return a 
 
	if (a > b): 
		return gcd(a-b, b) 
	return gcd(a, b-a) 

a = 48
b = 48
if(gcd(a, b)): 
	print('GCD of', a, 'and', b, 'is', gcd(a, b)) 
else: 
	print('not found') 

#Another Method 
def gcd(a,b): 
	
	if (b == 0): 
		return a 
	return gcd(b, a%b) 

a = 98
b = 78
if(gcd(a, b)): 
	print('GCD of', a, 'and', b, 'is', gcd(a, b)) 
else: 
	print('not found')
 
 
#Another Method
def hcf(a, b):
    
    if (a == 0):
        return b
    
    if (b == 0):
    	return a 

    if a < b:
        min = a
    else:
        min = b 
        
    for i in range(1, min + 1):
        
        if a % i == 0 and b % i == 0:
            hcf = i
    
    return hcf

if __name__ == "__main__":
	    
	print(f"HCF is {hcf(46, 1)}")

#using euclidean theorem
#gcd(a, b) = gcd(c, d) where c and d are smaller than a and b in ratio
#gcd(105, 91) = gcd(105%91, 91) = gcd(14, 91) = gcd(14, 91%14) = gcd(14, 7) = gcd(14%7, 7) = gcd(0, 7) = 7
#if a>b then (a%b,b) else (a, b%a)
def gcd(a, b):
	if a == b:
		return a
	elif a == 0:
		return b
	elif b == 0:
		return a

	if a>b:
		return gcd(a%b, b)
	else:
		return gcd(a, b%a)

if __name__ == "__main__":
	print(gcd(105, 91))