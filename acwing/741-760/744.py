c, sign = int(input()), input()

s = 0
for _ in range(12):
    l = list(map(float, input().split()))
    for i in range(12):
        if i == c:
            s += l[c]

if sign == "M":
    s /= 12

print(f"{s:.1f}")
