from math import sqrt

a, b, c = map(float, input().split())

p = (a + b + c) / 2
print(f"{sqrt(p*(p-a)*(p-b)*(p-c)):.1f}")
