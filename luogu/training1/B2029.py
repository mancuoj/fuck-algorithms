from math import ceil, pi

h, r = map(int, input().split())
print(f"{ceil(20000 / (pi*r*r*h))}")
