n = int(input())
arr = list(map(float, input().split()))

sum_val = sum(arr)
avr_res = sum_val / n

print(f"{avr_res:.1f}")
if avr_res >= 4.0:
    print("Perfect")
elif avr_res >= 3.0:
    print("Good")
else:
    print("Poor")