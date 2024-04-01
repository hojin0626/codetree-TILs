n = int(input())

i = 1
cnt = 0
arr = []
while cnt != 2:
    mux = n * i
    arr.append(mux)
    i += 1
    if mux % 5 == 0:
        cnt += 1

for ent in arr:
    print(ent, end=" ")