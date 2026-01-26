def sum_array(arr, n):
    # Base case
    if n == 0:
        return 0
    
    # Recursive call
    return arr[n - 1] + sum_array(arr, n - 1)

arr = [1, 2, 3, 4, 5]
print("Sum of array elements =", sum_array(arr, len(arr)))
