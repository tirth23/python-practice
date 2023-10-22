def bintodec(num):

    intnum = int(num)
    floatnum = round(num - intnum, 2)
    
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
        temp1 = str(floatnum)
        temp1 = temp1[2:]
        order1 = len(temp1)
        sum1 = 0
        temp1 = int(temp1)

        for i in range(-order1, 0):
            ans1 = temp1 % 10
            ans1 = ans1 * (2 ** i)
            sum1 = sum1 + ans1
            temp1 = temp1 // 10
        print(sum + sum1)

if __name__ == "__main__":

    #num = float(input("Enter binary number to convert it into decimal: "))
    num = 1100.01
    bintodec(num)