arr = input().split()
n = len(arr)

cnt = 0
sum_val = 0
for i in range(n):
    if int(arr[i]) < 250:
        sum_val += int(arr[i])
        cnt += 1
    else:
        break

print(sum_val, f"{sum_val/cnt:.1f}")