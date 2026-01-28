def cal_fact(n):
  if n == 0 or n == 1:
    return 1
  return n * cal_fact(n-1)

n = 5
print(cal_fact(n))