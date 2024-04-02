arr = list(map(int, input().split()))
a, b = arr[0], arr[1]

n = 10
count_arr = [0] * n
while a > 1:
    tmp = a % b
    # print(tmp)
    count_arr[tmp] += 1
    a //= b

# print(count_arr)
sum_val = 0
for i in range(n):
    sum_val += count_arr[i] * count_arr[i]

print(sum_val)