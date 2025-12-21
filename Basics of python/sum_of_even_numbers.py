num = int(input("Enter the range of numbers:"))
even_sum = 0
for i in range (1, num+1):
  if i % 2 == 0:
     even_sum += i
print("The sum of even numbers is:",even_sum)