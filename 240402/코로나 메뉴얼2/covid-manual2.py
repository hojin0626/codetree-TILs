hospital = [0] * 4

for _ in range(3):
    arr = input().split()
    arr[1] = int(arr[1])

    if arr[0] == 'Y':
        if arr[1] >= 37:
            hospital[0] += 1
        else:
            hospital[2] += 1
    else:
        if arr[1] >= 37:
            hospital[1] += 1
        else:
            hospital[3] += 1

for i in range(4):
    print(f"{hospital[i]}", end=" ")

if hospital[0] >= 2:
    print("E")