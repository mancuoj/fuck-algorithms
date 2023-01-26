n, k = map(int, input().split())

a, b = [], []
for i in range(1, n + 1):
    if i % k == 0:
        a.append(i)
    else:
        b.append(i)

print(f"{sum(a) / len(a):.1f} {sum(b) / len(b):.1f}")
