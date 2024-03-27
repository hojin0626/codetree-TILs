arr = input().split()
n = len(arr)

cnt = 0
sum_val = 0
for i in range(n):
    if int(arr[i]) >= 250:
        break
    sum_val += int(arr[i])
    cnt += 1

print(sum_val, f"{sum_val/cnt:.1f}")