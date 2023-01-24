from math import ceil

m, t, s = map(int, input().split())

if t == 0:
    print(0)
else:
    print(f"{0 if m - ceil(s / t) < 0 else m - ceil(s / t)}")
