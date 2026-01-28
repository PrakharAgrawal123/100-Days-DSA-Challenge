def print_num(n):
  if n == 0:
    return
  print(n)

  print_num(n-1)

n = 5
print_num(n)