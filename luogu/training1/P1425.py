a, b, c, d = map(int, input().split())
t = (c * 60 + d) - (a * 60 + b)

print(f"{t // 60} {t % 60}")
