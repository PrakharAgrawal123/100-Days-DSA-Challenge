def sum_of_num(n):
    if n == 0: # Base case
        return 0
    return n + sum_of_num(n - 1)

n = 5
print(sum_of_num(n))