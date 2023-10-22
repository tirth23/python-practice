def selection_sort(l):
    for i in range(len(l)):
        min_index = i
        for j in range(i+1, len(l)):
            if l[min_index] > l[j]:
                min_index = j
        
        l[i], l[min_index] = l[min_index], l[i]
    return l

if __name__ == "__main__":
    n = int(input("Enter number of elements to sort: "))
    print("Enter elements: ")
    l = [int(i) for i in input().split()]
    print("Sorted Array: ", selection_sort(l))
