arr1 = list(map(int, input().split()))
n, q = arr1[0], arr1[1]

arr2 = list(map(int, input().split()))

for _ in range(q):
    arr3 = list(map(int, input().split()))
    # print(arr3)
    if arr3[0] == 1:
        idx = arr3[1]
        print(arr2[idx - 1], end="")
    if arr3[0] == 2:
        if arr3[1] in arr2:
            idx = arr2.index(arr3[1])
            print(idx + 1, end="")
        else:
            print(0, end="")
    if arr3[0] == 3:
        s = arr3[1]
        e = arr3[2]
        for i in range(s - 1, e):
            print(arr2[i], end=" ")
    print()