def merge_sort(arr):
    if len(arr) > 1:
        midpoint = len(arr)//2
        LEFT = arr[:midpoint]
        RIGHT = arr[midpoint:]
        merge_sort(LEFT)
        merge_sort(RIGHT)

        i = j = k = 0
        while i < len(LEFT) and j < len(RIGHT):
            if LEFT[i] < RIGHT[j]:
                arr[k] = LEFT[i]
                i += 1
            else:
                arr[k] = RIGHT[j]
                j += 1
            k += 1
        
        while i < len(LEFT):
            arr[k] = LEFT[i]
            i += 1
            k += 1

        while j < len(RIGHT):
            arr[k] = RIGHT[j]
            j += 1
            k += 1
    
    return arr

arr = [15, 5, 24, 8, 1, 3, 16, 10, 20]
print(merge_sort(arr))