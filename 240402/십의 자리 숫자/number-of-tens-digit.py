arr = list(map(int, input().split()))

cnt_ten = [0] * 10
for elem in arr:
    if elem == 0:
        break
    t = elem // 10
    cnt_ten[t] += 1

for i in range(1, 10):
    print(f"{i} - {cnt_ten[i]}")