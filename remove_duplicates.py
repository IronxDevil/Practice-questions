arr = [1,1,2,2,3,3,3,4,5,5,6,7,7,7]
j = 0
for i in range(0, len(arr)):
    if j != arr[i]:
        arr[j] = arr[i]
        j += 1
arr = arr[: -(len(arr) - j)]
print(arr)