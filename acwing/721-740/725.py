from math import sqrt

n = int(input())

for _ in range(n):
    x = int(input())
    if x == 1:
        print(x, "is not perfect")
        continue

    total = 1
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            div = x / i
            if div == i:
                total += i
            else:
                total += i + div
    if total == x:
        print(x, "is perfect")
    else:
        print(x, "is not perfect")
