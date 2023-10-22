if __name__ == "__main__":
    string = input("Enter string to reverse : ")
    reverse = ""
    for i in range(len(string)-1,-1,-1):
        reverse = reverse + string[i]
    
    print(reverse)

    print(string[::-1])

    rev = ""
    for i in string:
        rev = i + rev
    print(rev)

    
    rev1 = ""
    for i in string:
        rev1 = rev1 + i
    print(rev1)

    