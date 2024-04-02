arr = list(map(int, input().split()))

cnt_dice = [0] * 7
for ent in arr:
    cnt_dice[ent] += 1

for i in range(1,7):
    print(f"{i} - {cnt_dice[i]}")