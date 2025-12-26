num = int(input("Enter the number:"))
count = 0
while num > 0:
  rem = num % 10
  num = num // 10
  count +=1
print(count)