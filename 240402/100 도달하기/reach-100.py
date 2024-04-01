n = int(input())
arr = [1, n]

i = 2
elem = 0
while elem < 100:
    elem = arr[i - 2] + arr[i - 1]
    arr.append(elem)
    i += 1

for ent in arr:
    print(ent, end=" ")