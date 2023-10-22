if __name__ == "__main__":
    
    row1 = int(input("Enter the row of matrix1 : "))
    col1 = int(input("Enter the column of matrix1 : "))
    print("Enter the values of first matrix : ")
    matrix1 = []
    for i in range(row1):
        colmat = []
        for j in range(col1):
            colt = int(input(f"Matrix1[{i}][{j}] : "))
            colmat.append(colt)
        print()
        matrix1.append(colmat)
    for i in range(row1):
        for j in range(col1):
            print(matrix1[i][j], end= " ")
        print()

    row2 = int(input("\nEnter the row of matrix2 : "))
    col2 = int(input("Enter the column of matrix2 : "))
    print("\nEnter the values of second matrix : ")
    matrix2 = []
    for i in range(row2):
        colmat = []
        for j in range(col2):
            colt = int(input(f"Matrix2[{i}][{j}] : "))
            colmat.append(colt)
        print()
        matrix2.append(colmat)
    for i in range(row2):
        for j in range(col2):
            print(matrix2[i][j], end= " ")
        print()
    
    ksum = row2 
    ans = [[0 for i in range(col2)] for j in range(row1)]
    print("\nMultiplication of both matrix : ")
    for i in range(row1):
        for j in range(col2):
            sum = 0
            for k in range(ksum):
                sum = sum + matrix1[i][k]*matrix2[k][j]
            ans[i][j] = sum
            #ans[i][j] = matrix1[i][0]*matrix2[0][j]+matrix1[i][1]*matrix2[1][j]+matrix1[i][2]*matrix2[2][j]
    for i in range(row1):
        for j in range(col2):
            print(ans[i][j], end=" ")
        print()