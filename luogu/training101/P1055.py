a, b, c, x = input().split("-")
n = a + b + c
sign = "0123456789X"

total = 0
for i in range(9):
    total += int(n[i]) * (i + 1)

if sign[total % 11] == x:
    print("Right")
else:
    print(f"{a}-{b}-{c}-{sign[total % 11]}")
