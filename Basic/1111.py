str1 = "An Apple a day keeps the doctor away."
print(str1[8::-3],str1[-2::1],str1[-1:-5:-1])
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
M = [[row[i] for row in matrix] for i in range(3)]
print(M)
for i in range(3):
    for row in matrix:
        print(row[i])

a=8
b="0"
print(a/b)