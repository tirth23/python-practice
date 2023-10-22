def swap(num):
    
    print(num)
    or1 = len(str(num))
    order = or1 - 1
    last = num % 10
    x = (pow(10, order))
    first = num // x
    print(first, last)
    
    num = num - last                        #unit digit = 0 
    num = num + first                       #add first digit
    num = num - (first * x)                 #first digit = 0 
    num = num + (last * x)                  #add last digit
    
    if last == 0:
        num = "0" + str(num)
    
    print(num)
        
if __name__ == "__main__":
    
    num = int(input("Enter number to swap first and last digit : "))
    swap(num)

#wih array
def swap(numbers):
    numbersList = []
    for number in str(numbers):
        numbersList.append(number)
    numbersList[0], numbersList[-1] = numbersList[-1], numbersList[0]
    return (''.join(numbersList))

print(swap(120))