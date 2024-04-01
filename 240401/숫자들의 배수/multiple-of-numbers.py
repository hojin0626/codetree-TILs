n = int(input())

i = 1
cnt = 0
while cnt != 2:
    mux = n * i
    i += 1
    print(mux, end=" ")
    if mux % 5 == 0:
        cnt += 1