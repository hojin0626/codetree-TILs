arr = list(map(int, input().split()))

sum_val = 0
cnt = 0
for i in arr:
    if i == 0:
        break
    sum_val += i
    cnt += 1

avg_res = sum_val / cnt
print(f"{sum_val} {avg_res:.1f}")