n = 10
arr1 = list(map(int, input().split()))
arr2 = []

sum_val = 0
for i in range(n):
    if arr1[i] == 0:
        break
    arr2.append(arr1[i])
    

for i in arr2[::-1]:
    print(i, end=" ")