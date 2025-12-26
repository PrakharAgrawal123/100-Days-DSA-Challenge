num = int(input("Enter the number:"))
m = num
rev = 0
while num > 0:
  rem = num % 10
  rev = rev *10 + rem
  num = num // 10
if m == rev:
  print("Palindrome Number")
else:
  print("Not a Palindrome")