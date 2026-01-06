def second_smallest_largest(nums):
    n = len(nums)
    
    if n < 2:
        return -1, -1

    smallest = float('inf')
    second_smallest = float('inf')
    largest = float('-inf')
    second_largest = float('-inf')

    for num in nums:
        # For smallest and second smallest
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num

        # For largest and second largest
        if num > largest:
            second_largest = largest
            largest = num
        elif second_largest < num < largest:
            second_largest = num

    if second_smallest == float('inf') or second_largest == float('-inf'):
        return -1, -1

    return second_smallest, second_largest
a = second_smallest_largest([1,2,2,5,6,7])
print(a)