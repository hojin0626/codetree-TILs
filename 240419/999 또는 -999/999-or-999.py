import sys
arr = list(map(int, input().split()))

min_val, max_val = sys.maxsize, -sys.maxsize
for elem in arr:
    if elem == 999 or elem == -999:
        break
    if elem > max_val:
        max_val = elem
    if elem < min_val:
        min_val = elem

print(max_val, min_val)