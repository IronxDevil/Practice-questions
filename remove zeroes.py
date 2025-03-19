arr = [0,1,5,0,0,0,3,4,8]
j = 0
for i in range (0, len(arr)):
    if arr[i] != 0:
        arr[j] = arr[i]
        j += 1
while j < len(arr):
    arr[j] = 0
    j += 1
print(arr)