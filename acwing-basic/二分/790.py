n = float(input())

l, r = -10010, 10010
# 保留四位小数，就是1e-6
# 保留六位小数，就是1e-8
# 同比增加两位
while r - l > 1e-8:
    mid = (l + r) / 2
    if mid**3 >= n:
        r = mid
    else:
        l = mid
print(f"{l:.6f}")
