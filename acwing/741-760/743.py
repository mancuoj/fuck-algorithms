l, sign = int(input()), input()

s = 0
for i in range(12):
    if i == l:
        s = sum(list(map(float, input().split())))
        break
    input()

if sign == "M":
    s /= 12

print(f"{s:.1f}")
