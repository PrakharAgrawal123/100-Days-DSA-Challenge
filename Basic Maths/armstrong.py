num = int(input("Enter a number: "))
m = num
n = len(str(num))
sum = 0

while m > 0:
    rem = m % 10
    sum += rem ** n
    m //= 10

if sum == num:
    print("Armstrong")
else:
    print("Not Armstrong")
