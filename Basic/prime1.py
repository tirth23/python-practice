number = int(input("Enter number to check whether it is prime or not : "))
if number > 1:
    is_prime = True
    for previousnumber in range(2, number):      #when 2 comes range(2,2) will come so loop will not be executed
        if number % previousnumber == 0:
            print(number, "is composite.")
            is_prime = False
            break
    if is_prime == True:
        print(number, "is prime.")
elif number == 1:
    print("1 is neither prime nor composite.")
else:
    print("Enter number greater than 1.")
    