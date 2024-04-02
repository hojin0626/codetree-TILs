n = int(input())
arr = list(map(int, input().split()))

cnt_arr = [0] * 10
for ent in arr:
    cnt_arr[ent] += 1

for ent in cnt_arr[1::]:
    print(ent)