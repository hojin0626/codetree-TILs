import sys

n1, n2 = tuple(map(int, input().split()))
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

for i in range(n1):
    ena = True
    for j in range(n2):
        if i + j >= n1:
            ena = False
            break

        if arr_a[i + j] != arr_b[j]:
            ena = False
            break
    if ena:
        print("Yes")
        sys.exit()

print("No")