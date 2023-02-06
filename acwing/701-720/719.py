n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x

    total = 0
    for i in range(x + 1, y):
        if i % 2 != 0:
            total += i
    print(total)
