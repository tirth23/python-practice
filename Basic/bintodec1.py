def bintodec(num):
    
    ind = num.find(".")
    if ind != -1:
        intnum = int(num[:ind])
        floatnum = num[ind+1:]
    else:
        intnum = int(num)
        floatnum = 0.0
    
    temp = intnum
    sum = 0
    order=len(str(intnum))
    for i in range(order):
        ans = temp % 10
        ans = ans * (2 ** i)
        sum = sum + ans
        temp = temp//10

    if floatnum == 0.0:
        print(sum)
    else:
        order1 = len(floatnum)
        temp1 = int(floatnum)
        sum1 = 0 
        
        for i in range(-order1, 0):
            ans1 = temp1 % 10
            ans1 = ans1 * (2 ** i)
            sum1 = sum1 + ans1
            temp1 = temp1 // 10
        print(sum + sum1)

if __name__ == "__main__":

    #num = float(input("Enter binary number to convert it into decimal: "))
    num = "1100.01"
    bintodec(num)