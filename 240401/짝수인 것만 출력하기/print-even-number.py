n = int(input())
arr = list(map(int, input().split()))

new_arr = []
for i in range(n):
    if arr[i] % 2 == 0:
        new_arr.append(arr[i])

for ent in new_arr:
    print(ent, end=" ")