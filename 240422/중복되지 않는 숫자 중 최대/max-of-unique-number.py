n = int(input())
arr = list(map(int, input().split()))

res = 0
max_res = arr[0]
for i in range(1, n):
    if arr[i] == max_res:
        res = -1
        continue
    elif arr[i] > max_res:
        max_res = arr[i]

if res == -1:
    print(res)
else:
    print(max_res)