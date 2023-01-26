from math import sqrt

n = int(input())

for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0:
        print(n // i)
        break
