from math import ceil

n = int(input())

price = []
for _ in range(3):
    a, b = map(int, input().split())
    price.append(ceil(n / a) * b)
print(min(price))
