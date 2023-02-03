c, sign = int(input()), input()

total = 0
for _ in range(12):
    l = list(map(float, input().split()))
    for i in range(12):
        if i == c:
            total += l[c]

if sign == "M":
    total /= 12

print(f"{total:.1f}")
