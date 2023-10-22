def decbin(num):
    
    intnum = int(num)
    floatnum = num - intnum
    print(floatnum)
    
    if floatnum == 0.0:
        bin1 = ""
        temp = intnum
        while temp != 0:
        
            ans2 = temp % 2
            temp = temp // 2
            bin1 = str(ans2) + bin1
        
    else: 
        bin = ""   
        ans = floatnum
        while ans != 0.0:             
            
            ans = ans * 2
            a = int(ans)
            bin = bin + str(a)
            ans = ans - a
        
        bin1 = "." + bin
            
        temp = intnum
        while temp != 0:
            
            ans2 = temp % 2
            temp = temp // 2
            bin1 = str(ans2) + bin1
        
    print(bin1)

if __name__ == "__main__":
    
    decimal = float(input("Enter decimal number to convert it to binary : "))
    decbin(decimal)