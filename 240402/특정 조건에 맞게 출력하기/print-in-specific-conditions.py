arr = list(map(int, input().split()))

new_arr = []
for ent in arr:
    if ent == 0:
        break
    if ent % 2 == 1:
        new_arr.append(ent + 3)
    else:
        new_arr.append(ent // 2)

for ent in new_arr:
    print(ent, end=" ")