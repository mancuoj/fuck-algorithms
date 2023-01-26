k = int(input())

s, n = 0, 0
while s <= k:
    n += 1
    s += 1 / n
print(n)
