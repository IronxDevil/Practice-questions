n = int(input("Rows: "))
element = 1
for j in range(1, n):
    print(element, end = " ")
    for i in range(1, j):
        element = (element * (j-i))//i
        print(element, end = " ")
    print()