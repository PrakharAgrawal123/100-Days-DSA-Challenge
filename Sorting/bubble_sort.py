arr = [4, 1, 5, 2, 3]
n = len(arr)
for i in range(n):
    swapped = False 
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            swapped = True

    if not swapped:
        break   # array already sorted

print(arr)
