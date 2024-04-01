arr = list(map(int, input().split()))

for i in range(10):
    a = arr[-2]
    b = arr[-1]
    # print(a, b)
    if (a + b) >= 10:
        arr.append(a + b - 10)
    else:
        arr.append(a + b)

for i in range(10):
    print(arr[i], end=" ")