def sort(arr):
	temp = 0
	for i in range(len(arr)):
		for j in range(len(arr)-1-i):
			if arr[j] > arr[j+1]:
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp
	arr2 = [None for i in range(len(arr))]
	j=0
	for i in range(len(arr)-1):
		if arr[i] != arr[i+1]:
			arr2[j] = arr[i]
			j += 1
	arr2[j] = arr[len(arr)-1]
	j += 1
	print(arr2)
	
arr = [10, 9, 8, 8, 20, 20, 20]
sort(arr)