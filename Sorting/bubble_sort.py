arr = [4,1,5,2,3]
n = 5
for i in range(0,n):
  for j in range(0,n-i-1):
    if arr[j] > arr[j+1]:
      temp = arr[j]
      arr[j] = arr[j+1]
      arr[j+1] = temp
print(arr)