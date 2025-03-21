arr = [1,1,2,2,3,3,3,4,5,5,6,7,7,7]
j = 1
for i in range(1, len(arr)):
    if arr[j] != arr[i - 1]:
        arr[j] = arr[i]
        
arr = arr[: -(len(arr) - j)]
print(arr)
print(j)