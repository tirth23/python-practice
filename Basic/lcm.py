# lcm(0,a) = 0 lcm(1, a) = a
def lcm(a, b):
    
    if a > b:
        max = a
    else:
        max = b

    if a == 0 or b == 0:
        return 0
        
    while(True):
        
        if max % a == 0 and max % b == 0:
            break
        max += 1
        
    return max
 
if __name__ == "__main__":
	
	print(f"LCM is {lcm(0, 30)}")