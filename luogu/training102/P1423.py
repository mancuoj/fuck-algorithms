s = float(input())

cnt, total, x = 0, 0, 2
while s > total:
    total += x
    x *= 0.98
    cnt += 1
print(cnt)
