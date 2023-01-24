from math import ceil

s, v = map(int, input().split())
t = 470 - ceil(s / v)

if t < 0:
    t = t + 24 * 60

print(f"{t // 60:02d}:{t % 60:02d}")
