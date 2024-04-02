arr1 = list(map(int, input().split()))
n, m = arr1[0], arr1[1]

arr2 = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if arr2[i] == m:
        cnt += 1

print(cnt)