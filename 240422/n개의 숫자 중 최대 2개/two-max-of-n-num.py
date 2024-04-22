n = int(input())
arr = list(map(int, input().split()))

tmp = 0
for i in range(n):
    m = n - i
    for j in range(1, m):
        if arr[j - 1] <= arr[j]:
            tmp = arr[j - 1]
            arr[j - 1] = arr[j]
            arr[j] = tmp

for res in arr[:2]:
    print(res, end=" ")