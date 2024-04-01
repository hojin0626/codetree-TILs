arr = list(map(int, input().split()))
n = len(arr)
arr1 = []

sum_val = 0
for i in range(n):
    if arr[i] == 0:
        arr1 = arr[i-3:i]
        sum_val = sum(arr1)
        break

print(sum_val)