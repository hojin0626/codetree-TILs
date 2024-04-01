n = int(input())
arr = list(map(int, input().split()))

new_arr = [ent * ent for ent in arr]

for i in range(n):
    print(new_arr[i], end=" ")