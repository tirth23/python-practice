def bubble_sort(l):
    n = len(l)
    for i in range(n):
        for j in range(n-1-i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    #print(l1 is l)
    return l
 
l1 = [40, 20, 50, 60, 30, 10]
bubble_sort(l1)
for i in range(len(l1)):
    print(l1[i], end=", ")
