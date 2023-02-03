l, sign = int(input()), input()

total = 0
for i in range(12):
    if i == l:
        total = sum(list(map(float, input().split())))
        break
    input()

if sign == "M":
    total /= 12

print(f"{total:.1f}")
