n = int(input())
arr = [1, n]

i = 2
ent = 0
while ent < 100:
    arr.append(arr[i - 2] + arr[i - 1])
    ent = arr[i]
    i += 1

for ent in arr:
    print(ent, end=" ")