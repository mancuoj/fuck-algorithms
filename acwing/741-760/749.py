sign = input()

s, cnt = 0, 0
for i in range(12):
    l = list(map(float, input().split()))
    for j in range(12):
        if j > i and i + j < 11:
            s += l[j]
            cnt += 1

if sign == "M":
    s /= cnt

print(f"{s:.1f}")
