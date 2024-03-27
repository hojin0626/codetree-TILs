student = int(input())

pass_cnt = 0
for _ in range(student):
    arr = list(map(int, input().split()))
    sum_val = sum(arr)
    avg_res = sum_val / len(arr)

    if avg_res >= 60:
        print("pass")
        pass_cnt += 1
    else:
        print("fail")

print(pass_cnt)