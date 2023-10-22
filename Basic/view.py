import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x)

for i in range(2,2):
    print("hello")


numList = [1,2,3,4,5]
alphaList = ["a","b","c","d","e"]
print(numList is alphaList)
print(numList == alphaList)
numList = alphaList
print(numList)
print(numList is alphaList)
print(numList == alphaList)