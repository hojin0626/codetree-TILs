n = int(input())
arr = list(map(int, input().split()))

for i in arr[n + 1::-1]:
    if i % 2 == 0:
        print(i, end=" ")