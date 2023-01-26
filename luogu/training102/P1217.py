from math import sqrt


def is_prime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


a, b = map(int, input().split())
c = [5, 7, 11]

for d1 in range(1, 10, 2):
    for d2 in range(10):
        x = d1 * 100 + d2 * 10 + d1
        if is_prime(x):
            c.append(x)

for d1 in range(1, 10, 2):
    for d2 in range(10):
        for d3 in range(10):
            x = d1 * 10000 + d2 * 1000 + d3 * 100 + d2 * 10 + d1
            if is_prime(x):
                c.append(x)

for d1 in range(1, 10, 2):
    for d2 in range(10):
        for d3 in range(10):
            for d4 in range(10):
                x = (
                    d1 * 1000000
                    + d2 * 100000
                    + d3 * 10000
                    + d4 * 1000
                    + d3 * 100
                    + d2 * 10
                    + d1
                )
                if is_prime(x):
                    c.append(x)

for i in range(len(c)):
    if a <= c[i] <= b:
        print(c[i])
    if c[i] > b:
        break
