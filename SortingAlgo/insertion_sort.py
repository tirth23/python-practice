def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = i-1
        while j >= 0 and val < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = val
    return arr

l = [9, 6, 7, 3, 2]
print(insertion_sort(l))