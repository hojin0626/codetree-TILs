arr = list(map(int, input().split()))

i = 2
elem = 0
while i != 10:
    elem = (2 * arr[i - 2]) + arr[i - 1]
    arr.append(elem)
    i += 1

for ent in arr:
    print(ent, end=" ")