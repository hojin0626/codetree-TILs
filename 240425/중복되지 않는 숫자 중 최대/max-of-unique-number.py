n = int(input())
arr = list(map(int, input().split()))

# arr.sort()
dup_arr = []
arr_cnt = {}

for k in arr:
    try:
        arr_cnt[k] += 1
    except:
        arr_cnt[k] = 1

for k, v in arr_cnt.items():
    if v >= 2:
        dup_arr.append(k)

max_res = 0
for i in range(n):
    if arr[i] in dup_arr:
        continue
    if arr[i] > max_res:
        max_res = arr[i]

if max_res == 0:
    print(-1)
else:
    print(max_res)