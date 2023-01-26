s = float(input())

cnt, sum, x = 0, 0, 2
while s > sum:
    sum += x
    x *= 0.98
    cnt += 1
print(cnt)
