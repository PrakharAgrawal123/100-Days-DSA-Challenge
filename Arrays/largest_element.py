arr = [10,20,30,40,50]
max = arr[0]
for i in range(len(arr)):
  if arr[i] > max:
    max = arr[i]
print("Largest element in an array is:",max)
