arr = list(map(int, input().split()))
a, b = arr[0], arr[1]

n = 10
count_arr = [0] * n
while a > 1:
    tmp = a % b
    count_arr[tmp] += 1
    a //= b

sum_val = 0
for i in range(n):
    sum_val += count_arr[i] * count_arr[i]

print(sum_val)