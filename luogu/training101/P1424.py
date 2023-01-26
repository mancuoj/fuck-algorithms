x, n = map(int, input().split())

# 本周剩余天数：7 + 1 - x
n -= 8 - x
print(
    f"{((8 - x - 2 if 8 - x - 2 > 0 else 0) + n // 7 * 5 + (5 if n % 7 > 5 else n % 7)) * 250}"
)
