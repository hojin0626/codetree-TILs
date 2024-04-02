arr = list(map(int, input().split()))

point_arr = [0] * 11
for p in arr:
    if p == 0:
        break
    if p < 10:
        continue
    t = p // 10
    point_arr[t] += 1

for i in range(10, 0, -1):
    print(f"{i}0 - {point_arr[i]}")