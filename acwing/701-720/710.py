x = int(input())

cnt = 0
while cnt < 6:
    if x % 2 != 0:
        print(x)
        cnt += 1
    x += 1
