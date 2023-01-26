x, y = 0, 0  # 自己手里的，妈妈手里的
for i in range(12):
    n = int(input())
    x += 300 - n
    if x < 0:
        print(-(i + 1))
        break
    else:
        while x >= 100:
            y += 100
            x -= 100
else:
    print(f"{int(y * 1.2) + x}")
